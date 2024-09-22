# Local Values in Terraform
locals {
  owners      = var.owners
  environment = var.environment
  name        = "${local.owners}-${local.environment}"
  tags = {
    owners      = local.owners
    environment = local.environment
  }
}