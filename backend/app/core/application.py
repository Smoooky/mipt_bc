from fastapi import FastAPI
from app.modules import register_modules
from app.core.middlewares import register_middlewares
from app.core.config import settings

class Application: 
    def __init__(self):
        self.fastapi_app = FastAPI(title=settings.APP_NAME)
    
    def setup(self):
        """Настройка приложения: роуты, middlewares и т.д."""
        register_middlewares(self.fastapi_app)
        register_modules(self.fastapi_app)

    def start(self):
        """Метод для запуска приложения через uvicorn"""
        import uvicorn
        uvicorn.run(self.fastapi_app, host=settings.APP_HOST, port=settings.APP_PORT)