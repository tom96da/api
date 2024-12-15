import pytest

from watsxn_trainup import WatsxnTrainup

class TestWatsxnTrainUp:
    def test_WatsxnTrainUp(self, base_app):
        WatsxnTrainup(base_app)
        assert base_app.extensions["watsxn-trainup"] is not None
        assert base_app.extensions["watsxn-trainup"].app is base_app
