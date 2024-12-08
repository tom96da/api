from flask import Flask
from watsxn_trainup import WatsxnTrainup

def create_app():
    app = Flask(__name__)

    WatsxnTrainup(app)

    @app.route("/")
    def index():
        return "<h1> Hello, Watsxn API! </h1>"

    return app

app = create_app()
