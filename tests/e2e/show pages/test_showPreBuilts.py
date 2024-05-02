from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showPreBuilts(test_app: FlaskClient):
    response = test_app.get('/preBuilts')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'Streaming/Recording' in response_data

