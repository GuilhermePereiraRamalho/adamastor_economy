from ninja import Schema
from typing import Optional
   
class UserIn(Schema):
    first_name: str
    last_name: str
    email: str
    password: str
    license_id: int  


class UserUpdate(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    license_id: Optional[int] = None

class UserOut(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    license_id: Optional[int] = None
    license_name: Optional[str] = None

    class Config:
        from_attributes = True