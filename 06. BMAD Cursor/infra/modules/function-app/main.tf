locals {
  name_prefix = "${var.project_name}-${var.environment}"
  location    = var.location

  default_tags = {
    ManagedBy  = "terraform"
    App        = var.project_name
    Env        = var.environment
    CostCenter = "engineering"
  }

  tags = merge(local.default_tags, var.tags)

  runtime_stack_map = {
    dotnet = "dotnet"
    node   = "node"
    python = "python"
    java   = "java"
  }
}

# --- Resource Group ---
resource "azurerm_resource_group" "this" {
  name     = "rg-${local.name_prefix}-${local.location}"
  location = local.location
  tags     = local.tags
}

# --- Storage Account (obrigatorio para Azure Functions) ---
resource "azurerm_storage_account" "this" {
  name                     = "st${replace(local.name_prefix, "-", "")}001"
  resource_group_name      = azurerm_resource_group.this.name
  location                 = azurerm_resource_group.this.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"

  blob_properties {
    delete_retention_policy {
      days = 7
    }
  }

  tags = local.tags
}

# --- App Service Plan (Consumption Y1) ---
resource "azurerm_service_plan" "this" {
  name                = "asp-${local.name_prefix}"
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  os_type             = "Linux"
  sku_name            = "Y1"

  tags = local.tags
}

# --- Azure Function App ---
resource "azurerm_linux_function_app" "this" {
  name                       = "func-${local.name_prefix}"
  resource_group_name        = azurerm_resource_group.this.name
  location                   = azurerm_resource_group.this.location
  service_plan_id            = azurerm_service_plan.this.id
  storage_account_name       = azurerm_storage_account.this.name
  storage_account_access_key = azurerm_storage_account.this.primary_access_key

  site_config {
    application_stack {
      node_version = var.function_runtime == "node" ? var.function_runtime_version : null
      python_version = var.function_runtime == "python" ? var.function_runtime_version : null
      dotnet_version = var.function_runtime == "dotnet" ? var.function_runtime_version : null
      java_version   = var.function_runtime == "java" ? var.function_runtime_version : null
    }

    ftps_state = "Disabled"
  }

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME"       = local.runtime_stack_map[var.function_runtime]
    "WEBSITE_RUN_FROM_PACKAGE"       = "1"
    "SCM_DO_BUILD_DURING_DEPLOYMENT" = "false"
  }

  identity {
    type = "SystemAssigned"
  }

  https_only = true

  tags = local.tags
}
