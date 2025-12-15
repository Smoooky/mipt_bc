from app.core.app import App

app_instance  = App()
app_instance.setup()

app = app_instance.fastapi_app

if __name__ == "__main__":
    app.start()