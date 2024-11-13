from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    class Config:
        env_file = '.env'
        extra = 'ignore'

settings = Settings()