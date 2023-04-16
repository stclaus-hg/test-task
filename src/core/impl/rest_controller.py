from typing import Dict, List, Union

from core.api.dtos import UserCreateModel, UserModel, UserUpdateModel
from fastapi.encoders import jsonable_encoder
from solution.profile import profile


class RestController:
    def __init__(self):
        self.db = profile.get_db_client()

    async def create_user(self, payload: UserCreateModel) -> UserModel:
        return await self.db.create_user(jsonable_encoder(payload))

    async def update_user(self, id: str, payload: UserUpdateModel) -> Union[UserModel, None]:
        return await self.db.update_user(id, jsonable_encoder(payload))

    async def delete_user(self, id: str) -> int:
        return await self.db.delete_user(id)

    async def users_list(self) -> List[UserModel]:
        return await self.db.get_all()
