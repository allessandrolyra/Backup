module "function_app" {
  source = "../../modules/function-app"

  project_name             = "teamai"
  environment              = "dev"
  location                 = "brazilsouth"
  function_runtime         = "python"
  function_runtime_version = "3.11"

  tags = {
    Owner      = "Projeto Team AI"
    CostCenter = "Team AI"
    Team       = "Estudio de Arquitetura"
  }
}

output "resource_group_name" {
  value = module.function_app.resource_group_name
}

output "storage_account_name" {
  value = module.function_app.storage_account_name
}

output "function_app_name" {
  value = module.function_app.function_app_name
}

output "function_app_url" {
  value = "https://${module.function_app.function_app_default_hostname}"
}
