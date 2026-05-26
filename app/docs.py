###--- PyDantic Schemas
# A sample payload for each one — both what goes in and what comes out.
"""
# 1. DocumentCreate — Client Sends This (Request Body)
json{
    "title": "DroHealth Refund Policy",
    "content": "Refunds are processed within 14 business days of the request. To initiate a refund, the patient must contact support with their transaction ID. Refunds are only applicable for consultations that were not completed...",
    "source": "support_docs"
}
This is what the client POSTs to /v1/documents. source is optional — they can omit it.

# 2. ChunkResponse — One Chunk Row (Response)
json{
    "id": 47,
    "source_document_id": "a3f1c2d4-89ab-4e21-bc34-7d9f0e123456",
    "title": "DroHealth Refund Policy",
    "source": "support_docs",
    "chunk_index": 2,
    "chunk_total": 5,
    "content": "Refunds are only applicable for consultations that were not completed due to a technical fault on our end.",
    "created_at": "2026-05-21T10:34:22"
}
Notice — no embedding field. Also notice chunk_index: 2 and chunk_total: 5 — meaning this is the 3rd chunk (0-based) out of 5 total chunks that the original document was split into.

# 3. DocumentSummary — Grouped Document (Response)
json{
    "source_document_id": "a3f1c2d4-89ab-4e21-bc34-7d9f0e123456",
    "title": "DroHealth Refund Policy",
    "source": "support_docs",
    "chunk_count": 5,
    "created_at": "2026-05-21T10:34:22"
}
All 5 chunk rows collapsed into one clean entry. The client just sees one document with a chunk count — the internal splitting is hidden.

# 4. IndexingResponse — Returned After Successful Upload (Response)
json{
    "source_document_id": "a3f1c2d4-89ab-4e21-bc34-7d9f0e123456",
    "title": "DroHealth Refund Policy",
    "chunk_count": 5,
    "message": "Document indexed successfully"
}
This is what comes back immediately after POST /v1/documents completes. It confirms the document was received, split into 5 chunks, and is now indexed and searchable.

# 5. ErrorResponse — When Something Goes Wrong (Response)
json{
    "code": "DOCUMENT_NOT_FOUND",
    "message": "No document found with source_document_id 'a3f1c2d4-89ab-4e21-bc34-7d9f0e123456'"
}
"""


