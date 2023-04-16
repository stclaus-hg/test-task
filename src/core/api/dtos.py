import datetime
from enum import Enum
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, validator


class UserRoleEnum(Enum):
    ADMIN = "admin"
    DEV = "dev"
    SIMPLE_MORTAL = "simple mortal"


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


def check_name_length(name: str) -> str:
    if name and (len(name) < 3 or len(name) > 100):
        print('Error')
        raise ValueError("Name should be more then 3 simbols and less then 100 simbols")
    return name


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    role: UserRoleEnum
    is_active: bool = True
    created_at: Optional[datetime.datetime]  # TODO: default value
    last_login: Optional[datetime.datetime]
    # hashed_pass: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        use_enum_values = True


class UserCreateModel(BaseModel):
    first_name: str
    last_name: str
    role: UserRoleEnum
    is_active: bool = True
    password: str

    _first_name = validator('first_name', allow_reuse=True, pre=True)(check_name_length)
    _last_name = validator('last_name', allow_reuse=True, pre=True)(check_name_length)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        use_enum_values = True


class UserUpdateModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[UserRoleEnum]
    is_active: Optional[bool]

    class Config:
        use_enum_values = True

    _first_name = validator('first_name', allow_reuse=True, pre=True)(check_name_length)
    _last_name = validator('last_name', allow_reuse=True, pre=True)(check_name_length)
