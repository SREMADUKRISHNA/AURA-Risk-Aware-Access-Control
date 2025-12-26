from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AccessRequest(BaseModel):
    """
    Schema for incoming access requests.
    """
    user_id: str = Field(..., description="Unique identifier for the user", example="user_12345")
    device_id: str = Field(..., description="Unique identifier for the device", example="dev_98765")
    ip_address: str = Field(..., description="IP address of the requester", example="192.168.1.10")
    location: str = Field(..., description="Geographic location string", example="New York, USA")
    login_time: datetime = Field(..., description="ISO 8601 timestamp of the login attempt")

class AccessResponse(BaseModel):
    """
    Schema for the risk engine decision response.
    """
    risk_score: float = Field(..., description="Calculated risk score between 0 and 100")
    decision: str = Field(..., description="Final access decision: ALLOW, STEP_UP_AUTH, or BLOCK")
    reason: str = Field(..., description="Human-readable explanation for the decision")
