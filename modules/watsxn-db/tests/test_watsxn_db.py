import pytest

from watsxn_db import WatsxnDB

def test_WatsxnDB(base_app):
    WatsxnDB(base_app)
    assert base_app.extensions["watsxn-db"] is not None
    assert base_app.extensions["watsxn-db"].app is base_app
    assert base_app.extensions["watsxn-db"].init_app
