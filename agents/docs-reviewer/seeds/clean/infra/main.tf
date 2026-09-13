variable "bucket_name" { type = string }
variable "table_name"  { type = string }

resource "aws_s3_bucket" "reports" {
  bucket        = var.bucket_name
  force_destroy = true
  tags          = { project = "report-indexer" }
}

resource "aws_dynamodb_table" "index" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "PK"
  range_key    = "SK"
  attribute { name = "PK" type = "S" }
  attribute { name = "SK" type = "S" }
  attribute { name = "customer_id" type = "S" }

  global_secondary_index {
    name            = "by-customer"
    hash_key        = "customer_id"
    projection_type = "KEYS_ONLY"
  }

  tags = { project = "report-indexer" }
}

resource "aws_cloudwatch_log_group" "indexer" {
  name              = "/report-indexer"
  retention_in_days = 14
  tags              = { project = "report-indexer" }
}
