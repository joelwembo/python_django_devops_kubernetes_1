terraform {
  backend "remote" {
    organization = "prodxcloud"
    workspaces {
      name = "prodxcloud"
    }
  }
}