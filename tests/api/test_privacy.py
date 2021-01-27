import json
from tests.conftest import client


def test_privacy(client):
    res = client.get('/privacy')
    assert res.status_code == 200
