from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showFAQ(test_app: FlaskClient):
    response = test_app.get('/faq')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''<p class="text-center mb-5">
      Find the answers for the most frequently asked questions below
    </p>''' in response_data
