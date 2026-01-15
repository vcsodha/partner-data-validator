from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional, Literal

class PartnerRow(BaseModel):
    partner_id: str
    name: str
    email: Optional[EmailStr]
    country: str
    status: Literal["active", "inactive"] = "active"
