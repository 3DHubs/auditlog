from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, Field

from .__version__ import __version__


class Session(BaseModel):
    """Session context"""

    id: str = Field(..., description="Session ID")
    issued_at: datetime = Field(..., description="Timestamp for session creation")
    issuer: str = Field(..., description="Issuer for the Session ID")
    attributes: Dict = Field({}, description="Extra attributes for this session")


class Identity(BaseModel):
    """Identity that caused the audit event"""

    id: str = Field(..., description="Unique identity ID as stored by issuer")
    name: str = Field(..., description="Friendly name for this identity")
    issuer: str = Field(..., description="Issuer for this identity")
    session: Optional[Session] = Field(None, description="Session context if available")


class AuditEvent(BaseModel):
    """Audit logging event"""

    version: str = Field(__version__, description="Audit event schema version")
    timestamp: datetime = Field(..., description="Timestamp for event generation")
    id: str = Field(..., description="Unique audit event ID")
    name: str = Field(..., description="Short audit event name")
    description: Optional[str] = Field("", description="Description for audit event")
    source: str = Field(..., description="Source for audit event")
    attributes: Dict = Field({}, description="Extra attributes for this event")
    identity: Identity
