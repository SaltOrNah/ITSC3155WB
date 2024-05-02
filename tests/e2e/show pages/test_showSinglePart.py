from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showSinglePart(test_app: FlaskClient):
    response = test_app.get('/parts/1', data = {'part_id': '1'})
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''<p class="card-text">Price: $''' in response_data

