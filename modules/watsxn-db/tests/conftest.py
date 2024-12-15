import shutil
import tempfile
import pytest

from flask import Flask
from sqlalchemy_utils.functions import create_database, database_exists

from watsxn_db import WatsxnDB, db as db_

@pytest.fixture()
def instance_path():
    """Temporary instance path fixture."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)

@pytest.fixture
def base_app(instance_path):
    """Base application fixture."""
    app_ = Flask("testapp", instance_path=instance_path)
    app_.config.update(
        SQLALCHEMY_DATABASE_URI="postgresql://tom96da:dbpass@localhost:5432/tom96da_test"
    )
    return app_

@pytest.fixture
def app(base_app: Flask):
    """Application fixture."""
    WatsxnDB(base_app)

    with base_app.app_context():
        yield base_app

@pytest.fixture
def client(app: Flask):
    """Test client fixture."""
    return app.test_client()

@pytest.fixture
def db(app: Flask):
    """Database fixture."""
    if not database_exists(db_.engine.url):
        create_database(db_.engine.url)
    db_.create_all()
    yield db_
    db_.session.remove()
    db_.drop_all()
