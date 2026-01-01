from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'mipt_bc'
    DEBUG: bool = True

    # Дальше много настроек
    APP_PORT: int
    APP_HOST: str

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str

    REGISTRATION_PAGE_URL: str

    class Config:
        env_file = '../../.env'

settings = Settings()