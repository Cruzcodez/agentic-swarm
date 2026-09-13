# report-indexer

Indexes PDF reports from S3 into DynamoDB.

## Running it

```bash
python indexer.py --bucket my-bucket
```

## Limitations

- Only handles PDF. Other formats are skipped.
- Single-threaded. Large buckets take a while.
