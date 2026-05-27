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

#. Alembic: `alembic revision --autogenerate -m "create_documents_table"`

# Sample payloads to create document
'''
// {
//   "title": "Acme Corp Customer FAQ",
//   "source": "faq",
//   "content": "  What is your refund policy? We offer a 30-day full refund on all purchases. To request a refund, contact support@acme.com with your order number. Refunds are processed within 5-7 business days.\n\nHow do I reset my password? Visit the login page and click 'Forgot Password'. Enter your registered email and we will send a reset link within 2 minutes. The link expires after 24 hours.\n\nDo you offer customer support on weekends? Yes, our support team is available Monday to Saturday, 8am to 6pm WAT. For urgent issues outside these hours, email urgent@acme.com.\n\nHow do I upgrade my subscription? Log into your dashboard, navigate to Billing, and select Upgrade Plan. Changes take effect immediately and you are only charged the prorated difference.\n\nCan I use the product on multiple devices? Yes, your account supports up to 5 devices simultaneously. You can manage connected devices from the Account Settings page.  "
// }

// {
//   "title": "Common Drug Interactions Guide",
//   "source": "medical_docs",
//   "content": "Warfarin and Aspirin: Combining warfarin with aspirin significantly increases the risk of bleeding. Patients on warfarin should avoid aspirin unless specifically directed by their physician. Regular INR monitoring is essential.\n\nMetformin and Alcohol: Alcohol consumption while taking metformin increases the risk of lactic acidosis. Patients should limit or avoid alcohol entirely. Symptoms of lactic acidosis include nausea, weakness, and difficulty breathing.\n\nSSRIs and MAOIs: Combining SSRIs such as fluoxetine with MAOIs can cause serotonin syndrome, a potentially life-threatening condition. A washout period of at least 14 days is required when switching between these drug classes.\n\nStatins and Grapefruit Juice: Grapefruit juice inhibits the enzyme CYP3A4 which metabolises many statins including atorvastatin and simvastatin. This raises statin levels in the blood and increases the risk of muscle damage."
// }

// {
//   "title": "Employee Leave Policy 2025",
//   "source": "hr_policy",
//   "content": "Annual Leave: Full-time employees are entitled to 20 working days of annual leave per year. Leave must be approved by the line manager at least 5 working days in advance. Unused leave of up to 10 days may be carried over to the next calendar year.\n\nSick Leave: Employees are entitled to 10 days of paid sick leave annually. A medical certificate is required for absences exceeding 3 consecutive days. Sick leave does not carry over to the following year.\n\nMaternity and Paternity Leave: Primary caregivers are entitled to 16 weeks of paid maternity leave. Secondary caregivers are entitled to 2 weeks of paid paternity leave. Both must be taken within 6 months of the child's birth or adoption.\n\nRemote Work Policy: Employees may work remotely up to 3 days per week subject to manager approval. All remote workers must be reachable during core hours of 10am to 3pm in their local timezone. Equipment for remote work is provided by the company upon request."
// }


'''
