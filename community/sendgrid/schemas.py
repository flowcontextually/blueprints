from pydantic import BaseModel, Field
from typing import List, Optional


# Define base/component models FIRST, so they exist when the composite model is defined.
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
    """Defines recipients and subject for an email envelope."""

    to: List[EmailObject]
    cc: Optional[List[EmailObject]] = None
    bcc: Optional[List[EmailObject]] = None
    subject: str


# Define the final, top-level model LAST.
class SendGridMailPayload(BaseModel):
    """The top-level Pydantic model for the SendGrid v3 Mail Send API."""

    personalizations: List[Personalization]
    from_email: EmailObject = Field(..., alias="from")
    content: List[Content]
    attachments: Optional[List[Attachment]] = None

    class Config:
        populate_by_name = True
