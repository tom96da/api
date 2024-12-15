import pytest

from watsxn_trainup.views import blueprint


def test_index(client):
    response = client.get("/trainup/")
    assert response.status_code == 200
    assert b"<h1>Watsxn TrainUp</h1>" in response.data
