from typing import Dict, List, Union

from bson import ObjectId
from core.api.dtos import UserModel, UserUpdateModel
from core.spi.db_client import DBClientSPI

import motor.motor_asyncio


class DBClient(DBClientSPI):
    USER_COLLECTION = "users"

    def __init__(self, connection_uri: str, port: int, database: str):
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri, port)
        db = client[database]
        self.users = db[self.USER_COLLECTION]

    async def get_all(self) -> List[Dict]:
        return [UserModel(**document) async for document in self.users.find(projection={"hashed_pass": 0})]

    async def create_user(self, user: dict) -> dict:
        user["hashed_pass"] = user.pop("password")
        new_user = await self.users.insert_one(user)
        created_user = await self.users.find_one({"_id": new_user.inserted_id}, projection={"hashed_pass": 0})
        return UserModel(**created_user)

    async def update_user(self, id: str, user: dict) -> Union[Dict, None]:
        user = {k: v for k, v in user.items() if v is not None}

        if user:
            update_result = await self.users.update_one({"_id": ObjectId(id)}, {"$set": user})

            if update_result.modified_count == 1:
                if (
                    updated_user := await self.users.find_one({"_id": ObjectId(id)}, projection={"hashed_pass": 0})
                ) is not None:
                    return UserModel(**updated_user)

        if (existing_user := await self.users.find_one({"_id": ObjectId(id)}, projection={"hashed_pass": 0})) is not None:
            return UserModel(**existing_user)

        return None

    async def delete_user(self, id: str) -> int:
        delete_result = await self.users.delete_one({"_id": ObjectId(id)})
        return delete_result.deleted_count
