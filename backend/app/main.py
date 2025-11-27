from backend.app.core.app import App

app = App()
app.setup()

if __name__ == "__main__":
    app.start()