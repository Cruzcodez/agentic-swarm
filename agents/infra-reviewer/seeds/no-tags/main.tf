resource "aws_lambda_function" "fn" {
  function_name = "fn-${random_id.suffix.hex}"
  runtime       = "python3.12"
  handler       = "handler.main"
  role          = aws_iam_role.fn.arn
  filename      = "build/fn.zip"
}

resource "aws_cloudwatch_log_group" "fn" {
  name              = "/aws/lambda/fn-${random_id.suffix.hex}"
  retention_in_days = 0
}

resource "random_id" "suffix" {
  byte_length = 4
}
