import pytest

from watsxn_db import WatsxnDB

class TestWatsxnDB:
    def test_WatsxnDB(self,base_app):
        WatsxnDB(base_app)
        assert base_app.extensions["watsxn-db"] is not None
        assert base_app.extensions["watsxn-db"].app is base_app
        assert base_app.config["SQLALCHEMY_DATABASE_URI"]
