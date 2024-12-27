from pydantic import BaseModel, EmailStr
from typing import Optional


# Base schema for users
class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    role: Optional[int] = 2

    class ConfigDict:
        from_attributes = True


# Schema for user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    role: Optional[int] = 2

    class ConfigDict:
        from_attributes = True
