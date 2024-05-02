from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showStartBuild(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.get('/startBuild/motherboard')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''<li class="nav-item">
                <a class="nav-link border .bg-light fw-bold text-success" href="/startBuild/motherboard">Motherboard</a>
              </li>''' in response_data

def test_showStartBuild_with_search(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.get('/startBuild/motherboard?q=i&sh=all&st=rating')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''<h5 class="card-title">Cooling 2</h5>''' in response_data