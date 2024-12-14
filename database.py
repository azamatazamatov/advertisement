from pymongo import MongoClient

# Параметры подключения к MongoDB
MONGO_DETAILS = "mongodb://root:example@localhost:27017"

# Подключаемся к базе данных
client = MongoClient(MONGO_DETAILS)
database = client['mydatabase']  # Используйте свое имя базы данных
