from dataclasses import dataclass, fields
from typing import Callable

from core.spi.db_client import DBClientSPI

from ._motor import get_db_client


@dataclass
class AppProfile:
    get_db_client: Callable[[], DBClientSPI] = None


profile = AppProfile()

profile.get_db_client = get_db_client


for field in fields(AppProfile):
    assert getattr(profile, field.name), f"app profile do not define {field.name}"
