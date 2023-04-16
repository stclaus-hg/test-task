import os

LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL", "DEBUG").lower()

REST_SERVER_PORT = int(os.environ.get("REST_SERVER_PORT", 6776))
REST_SERVER_HOST = os.environ.get("REST_SERVER_HOST", "0.0.0.0")


MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost/?retryWrites=true&w=majority")
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(os.environ.get("MONGO_PORT", "27017"))
DB_NAME = os.environ.get("DB_NAME", "test-task")
