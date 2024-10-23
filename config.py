import os
from dotenv import dotenv_values
from dotenv import load_dotenv


# Подгрузка файла .env 
_dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(_dotenv_path):
    load_dotenv(_dotenv_path)

# Создание словаря значений
_config = dotenv_values()


# Переменные для конфигурации
TOKEN = _config["BOT_TOKEN"]

