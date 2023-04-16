from abc import ABC, abstractmethod

from core.api.dtos import UserModel


class DBClientSPI(ABC):
    @abstractmethod
    async def create_user(self, payload: UserModel) -> str:
        pass
