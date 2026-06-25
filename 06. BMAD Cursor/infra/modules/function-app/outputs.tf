output "resource_group_name" {
  value       = azurerm_resource_group.this.name
  description = "Nome do Resource Group criado"
}

output "resource_group_id" {
  value       = azurerm_resource_group.this.id
  description = "ID do Resource Group"
}

output "storage_account_name" {
  value       = azurerm_storage_account.this.name
  description = "Nome do Storage Account"
}

output "storage_account_id" {
  value       = azurerm_storage_account.this.id
  description = "ID do Storage Account"
}

output "function_app_name" {
  value       = azurerm_linux_function_app.this.name
  description = "Nome da Function App"
}

output "function_app_default_hostname" {
  value       = azurerm_linux_function_app.this.default_hostname
  description = "Hostname padrao da Function App"
}

output "function_app_identity_principal_id" {
  value       = azurerm_linux_function_app.this.identity[0].principal_id
  description = "Principal ID da Managed Identity da Function"
}
