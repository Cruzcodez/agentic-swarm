resource "aws_s3_bucket" "reports" {
  bucket = "acme-report-indexer-reports"
}

resource "aws_dynamodb_table" "index" {
  name         = "report-index"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "PK"
  range_key    = "SK"
  attribute { name = "PK" type = "S" }
  attribute { name = "SK" type = "S" }
}

resource "aws_cloudwatch_log_group" "indexer" {
  name              = "/indexer"
  retention_in_days = 0
}

resource "aws_iam_role" "indexer" {
  name               = "report-indexer-role"
  assume_role_policy = data.aws_iam_policy_document.assume.json
}
