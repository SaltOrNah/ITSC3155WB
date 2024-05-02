from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showSinglePc(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/save_build', data = {'build_id': '1'}, follow_redirects=True)
    response = test_app.get('/singlePC/1', data = {'build_id': '1'})
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''<p class="card-text">Estimate: $1244.49''' in response_data