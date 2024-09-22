terraform {
  backend "remote" {
    organization = "prodxcloud"
    token = "kbrAiDdnwCKEYg.atlasv1.9COhLimGMbbyuQVLFk2ZT7ezuIZ63UfaXl6DsUCTtD9ISmWLHnDk02Vt68DcACPY7W4"
    workspaces {
      name = "prodxcloud"
    }
  }
}