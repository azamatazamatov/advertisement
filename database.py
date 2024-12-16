from pymongo import MongoClient
from sqlalchemy.ext.declarative import declarative_base

# Параметры подключения к MongoDB
MONGO_DETAILS = "mongodb://root:example@localhost:27017"

# Подключаемся к базе данных
client = MongoClient(MONGO_DETAILS)
database = client['mydatabase']  # Используйте свое имя базы данных
Base = declarative_base()