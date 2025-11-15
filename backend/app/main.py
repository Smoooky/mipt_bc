from app.core.application import Application

app = Application()
app.setup()

if __name__ == "__main__":
    app.start()