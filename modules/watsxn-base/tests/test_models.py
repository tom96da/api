import pytest
from watsxn_base.models import User

@pytest.fixture
def user_data():
    """ Fixture for user data. """
    return {"username": "testuser", "password": "testpass"}


# .tox/c1/bin/pytest --cov=watsxn_base tests/test_models.py::TestUser -v -vv -s --cov-branch --cov-report=term --cov-report=html --basetemp=.tox/c1/tmp --full-trace
class TestUser:
    """ Test cases for watxsn_base.models.User. """

    # .tox/c1/bin/pytest --cov=watsxn_base tests/test_models.py::TestUser::test_count -v -vv -s --cov-branch --cov-report=term --cov-report=html --basetemp=.tox/c1/tmp --full-trace
    def test_count(self, db):
        """ Test for User.count(). """
        assert User.count() == 0
        user = User(username="testuser", password="testpass")
        db.session.add(user)
        db.session.commit()
        print(f"user.created_at: {user.created}")
        print(f"type(user.created_at): {type(user.created)}")
        assert User.count() == 1

    # .tox/c1/bin/pytest --cov=watsxn_base tests/test_models.py::TestUser::test_create -v -vv -s --cov-branch --cov-report=term --cov-report=html --basetemp=.tox/c1/tmp --full-trace
    def test_create(self, db, user_data):
        """ Test for User.create(). """
        user = User.create(**user_data)
        assert user.username == user_data["username"]
        assert user.password == user_data["password"]
        assert User.count() == 1

