#!/usr/bin/env bash
# Deploys everything. Run once.
cd infra && terraform apply -auto-approve
# The CloudWatch dashboard has to be made by hand in the console; terraform
# doesn't support the widget layout we want. Name it "report-indexer-ops".
# Also create the SNS topic "report-indexer-alerts" manually and subscribe
# the on-call email.
