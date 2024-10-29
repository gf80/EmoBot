from pydantic_settings import BaseSettings

class Config(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str

    class Config:
        env_file = ".env"
