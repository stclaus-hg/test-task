import config
import uvicorn
from solution.channel.fastapi.app import get_app

if __name__ == '__main__':
    uvicorn.run(get_app(), host=config.REST_SERVER_HOST, port=config.REST_SERVER_PORT, log_level=config.LOGGER_LEVEL)
