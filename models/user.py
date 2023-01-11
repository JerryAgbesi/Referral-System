from pydantic import BaseModel,EmailStr
import datetime

class User(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    token: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


