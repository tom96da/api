from flask import Flask
from watsxn_db import WatsxnDB
from watsxn_db.cli import register_db_commands
from watsxn_trainup import WatsxnTrainup

def create_app():
    app = Flask(__name__)

    WatsxnDB(app)
    WatsxnTrainup(app)

    register_db_commands(app)

    @app.route("/")
    def index():
        return "<h1> Hello, Watsxn API! </h1>"

    return app

app = create_app()
