from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'mipt_bc'
    DEBUG: bool = True

    # Дальше много настроек
    APP_PORT: int
    APP_HOST: str

    class Config:
        env_file = '../../.env'

settings = Settings()