from apps.settings import app
from apps.person_app import home

app.register_blueprint(home)

if __name__ == "__main__":
    app.run()
