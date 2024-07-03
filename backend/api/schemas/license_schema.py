from ninja import Schema
from typing import Optional

class LicenseIn(Schema):
    name: str

class LicenseUpdate(Schema):
    name: Optional[str] = None

class LicenseOut(Schema):
    id: int
    name: str

    class Config:
        from_attributes = True