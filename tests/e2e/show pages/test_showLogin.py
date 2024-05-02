from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showLogin(test_app: FlaskClient):
    response = test_app.get('/login')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200

def test_showLogin_while_in(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.get('/login')
    response_data = response.data.decode('utf-8')
    #Can't return
    assert response.status_code == 302
    
def test_logOut(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/')
    response = test_app.get('/')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''Login</a>'''in response_data

