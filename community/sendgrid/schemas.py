# Schemas for the SendGrid v3 Mail Send endpoint
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional


class EmailObject(BaseModel):
    """Represents an email address with an optional name."""

    email: str
    name: Optional[str] = None


class Content(BaseModel):
    """Represents the HTML content of the email."""

    type: str = Field("text/html", description="The MIME type of the content.")
    value: str = Field(..., description="The actual HTML body.")


class Attachment(BaseModel):
    """Represents a single file attachment."""

    content: str = Field(..., description="The Base64 encoded content of the file.")
    filename: str
    type: Optional[str] = None
    disposition: str = Field(
        "attachment", description="Should be 'attachment' for files."
    )


class Personalization(BaseModel):
    """Defines the recipients (to, cc, bcc) and subject for an email envelope."""

    to: List[EmailObject]
    cc: Optional[List[EmailObject]] = None
    bcc: Optional[List[EmailObject]] = None  # Added for completeness
    subject: str


class SendGridMailPayload(BaseModel):
    """
    The top-level Pydantic model for the SendGrid v3 Mail Send API.
    This is the model that the engine will build and validate against.
    """

    personalizations: List[Personalization]
    # The 'alias' is critical because 'from' is a reserved keyword in Python.
    from_email: EmailObject = Field(..., alias="from")
    content: List[Content]
    attachments: Optional[List[Attachment]] = None

    class Config:
        # Allows using 'from_email' in Python code while serializing to 'from' in JSON.
        populate_by_name = True
