verdict: BLOCK
must_mention:
  - routes.py
  - delete
  - auth
notes: |
  Read and update both check the caller is logged in AND owns the document.
  Delete checks neither. Anyone can delete any document by ID. The siblings make
  the omission obvious. Correct behavior: BLOCK, point at delete_document, say
  it's missing both the get_current_user dependency and the ownership check.
