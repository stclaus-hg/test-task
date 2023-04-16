import config
from core.spi.db_client import DBClientSPI
from solution.sp.motor import DBClient


def get_db_client() -> DBClientSPI:
    return DBClient(config.MONGO_URI, config.MONGO_PORT, config.DB_NAME)
