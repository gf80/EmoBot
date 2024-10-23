import os
from dotenv import dotenv_values
from dotenv import load_dotenv


# Подгрузка файла .env 
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Создание словаря значений
config = dotenv_values()


# Переменные для конфигурации
TOKEN = config["BOT_TOKEN"]

