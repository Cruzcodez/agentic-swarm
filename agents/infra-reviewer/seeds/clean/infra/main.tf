terraform {
  required_version = ">= 1.5"
  backend "s3" {
    # State lives in a versioned bucket with a lock table, so every CI run and
    # every teardown sees the same record of what exists. Values are supplied
    # by -backend-config at init time; nothing account-specific is committed.
    key = "report-indexer/terraform.tfstate"
  }
}

variable "project" { type = string }
variable "bucket_name" { type = string }

resource "aws_s3_bucket" "reports" {
  bucket        = var.bucket_name
  force_destroy = true
  tags = {
    project = var.project
    purpose = "raw report storage"
  }
}

resource "aws_cloudwatch_log_group" "indexer" {
  name              = "/${var.project}/indexer"
  retention_in_days = 14
  tags              = { project = var.project }
}
