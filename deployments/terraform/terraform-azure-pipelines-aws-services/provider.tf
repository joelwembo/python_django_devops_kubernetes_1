terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.6" # which means any version equal & above
    }
  }
  required_version = ">= 0.13"
}

provider "aws" {
  region = var.region
  #   profile = "default" #AWS Credentials Profile (profile = "default") configured on local
  #   access_key = var.aws_access_key
  #   secret_key = var.aws_secret_key
}