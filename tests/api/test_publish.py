import json
from tests.conftest import client


def test_publish_no_query_params_400(client):
    res = client.post('/api/v1/publish')
    assert res.status_code == 400


def test_publish_with_body(client):
    data = {"data": "base64-encoded picture"}
    res = client.post('/api/v1/publish', json=data)
    assert res.status_code == 201


def test_publish_response_contains_link(client):
    data = {"data": "base64-encoded picture"}
    res = client.post('/api/v1/publish', json=data)
    link = res.json['_link']
    assert 'https://' in link

