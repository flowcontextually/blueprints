# Schemas for the SendGrid v3 Mail Send endpoint
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional

class EmailObject(BaseModel):
    email: str
    name: Optional[str] = None

class Personalization(BaseModel):
    to: List[EmailObject]
    cc: Optional[List[EmailObject]] = None
    subject: str

class Attachment(BaseModel):
    content: str # Base64 encoded content
    filename: str
    type: Optional[str] = None
    disposition: str = "attachment"

class Content(BaseModel):
    type: str = "text/html"
    value: str

class SendGridMailPayload(BaseModel):
    """Pydantic model for the SendGrid v3 Mail Send API."""
    personalizations: List[Personalization]
    from_email: EmailObject = Field(..., alias="from")
    content: List[Content]
    attachments: Optional[List[Attachment]] = None
