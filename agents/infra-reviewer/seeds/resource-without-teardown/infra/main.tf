resource "aws_s3_bucket" "reports" {
  bucket = var.bucket_name
  tags   = { project = "report-indexer" }
}

resource "aws_dynamodb_table" "index" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "PK"
  attribute { name = "PK" type = "S" }
  tags = { project = "report-indexer" }
}
