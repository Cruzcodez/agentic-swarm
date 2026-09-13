# 2. DynamoDB single-table for the report index

**Status:** Accepted

## Context

Reports need two access patterns: fetch one by report ID, and list all reports
for a customer. Volume is low. Nobody wants to run a database server for a
proof of concept.

## Decision

One DynamoDB table. PK is the report ID. SK is `META` for the summary item
and `PAGE#n` for each page. A global secondary index on `customer_id`
(keys only) handles the list-by-customer pattern.

## Consequences

Cheap and zero-ops. A third access pattern later means another GSI or a
redesign. Acceptable for a proof of concept. Would revisit before production.
