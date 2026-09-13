#!/usr/bin/env bash
set -e
aws s3 sync ./out s3://moneyiseasy-dev-frontend --delete
aws cloudfront create-invalidation --distribution-id E2RWLWPRVUGKRX --paths "/*"
aws lambda update-function-code \
  --function-name arn:aws:lambda:us-east-1:123456789012:function:api-handler \
  --zip-file fileb://build/api.zip
