variable "project_name" {
  type        = string
  description = "Nome do projeto/aplicacao"

  validation {
    condition     = can(regex("^[a-z0-9]{3,15}$", var.project_name))
    error_message = "project_name deve conter apenas letras minusculas e numeros (3-15 chars)."
  }
}

variable "environment" {
  type        = string
  description = "Ambiente: dev, stg ou prd"

  validation {
    condition     = contains(["dev", "stg", "prd"], var.environment)
    error_message = "environment deve ser dev, stg ou prd."
  }
}

variable "location" {
  type        = string
  description = "Regiao Azure (ex: eastus2, brazilsouth)"
  default     = "eastus2"
}

variable "function_runtime" {
  type        = string
  description = "Runtime da Function: dotnet, node, python, java"
  default     = "node"

  validation {
    condition     = contains(["dotnet", "node", "python", "java"], var.function_runtime)
    error_message = "function_runtime deve ser dotnet, node, python ou java."
  }
}

variable "function_runtime_version" {
  type        = string
  description = "Versao do runtime (ex: ~4 para node, v4.0 para dotnet, 3.11 para python)"
  default     = "~4"
}

variable "tags" {
  type        = map(string)
  description = "Tags obrigatorias para governanca e FinOps"
  default     = {}
}
