terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.97.0"
    }
  }
  backend "azurerm" {
    subscription_id      = "7a10c5e9-76b4-417b-9f21-ccad0bc5596f"
    resource_group_name  = "rg-rootsacad2022-workshop"
    storage_account_name = "sarootsacad2022workshop"
    container_name       = "statecontainerbrt"
    key                  = "azure-rootsacademy.tfstate"
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_storage_container" "brt" {
  name                  = "brt"
  storage_account_name  = "sarootsacad2022workshop"
  container_access_type = "private"
}
