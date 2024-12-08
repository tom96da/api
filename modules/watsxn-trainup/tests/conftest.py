import pytest
from flask import Flask
from watsxn_trainup.views import blueprint

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app

@pytest.fixture
def client(app):
    return app.test_client()
