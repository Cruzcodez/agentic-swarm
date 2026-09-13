from fastapi import APIRouter, Depends, HTTPException
from .auth import get_current_user
from .db import documents

router = APIRouter()


@router.get("/documents/{doc_id}")
def read_document(doc_id: str, user=Depends(get_current_user)):
    doc = documents.get(doc_id)
    if not doc:
        raise HTTPException(404)
    if doc.owner_id != user.id:
        raise HTTPException(403)
    return doc


@router.put("/documents/{doc_id}")
def update_document(doc_id: str, body: dict, user=Depends(get_current_user)):
    doc = documents.get(doc_id)
    if not doc:
        raise HTTPException(404)
    if doc.owner_id != user.id:
        raise HTTPException(403)
    documents.update(doc_id, body)
    return {"ok": True}


@router.delete("/documents/{doc_id}")
def delete_document(doc_id: str):
    documents.delete(doc_id)
    return {"ok": True}
