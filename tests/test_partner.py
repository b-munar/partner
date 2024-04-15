import pytest
from unittest.mock import patch
from functools import wraps

import uuid

import json

partner_uuid = uuid.uuid4()

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : str(partner_uuid)}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/partner/ping")
    assert response.status_code == 200
    assert b"pong" in response.data


def test_request_post_partner(client):
    url = "/partner"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "user": str(partner_uuid),
        "name": "parnert",
        "last_name": "parnert",
        "age": 20,
        "profession": "cowboy",
        "license": "Hunter X",
        "identification_type": "CC",
        "identification": "314159",
        "country_birth": "Colombia",
        "city_birth": "Cali",
        "country_residence": "Colombia",
        "city_residence": "Elvira",
        "sports": ["basketball"],
        "companies": ["Uniandes"],
        "type_services": ["education"]
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201

def test_request_get_partner(client):
    url = "/partner"
    headers = {
        "Content-Type": "application/json"
    }
    response = client.get(url, headers=headers)
    assert response.status_code == 200