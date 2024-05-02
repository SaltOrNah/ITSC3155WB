from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_show_saves(test_app: FlaskClient):
    response = test_app.get('/show_saves')
    response_data = response.data.decode('utf-8')
    #page exist, but can't access as redirected
    assert response.status_code == 302
    
def test_save_build_e2e(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/save_build', data = {'build_id': '1'}, follow_redirects=True)
    response = test_app.get('/show_saves')
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '''<div class="col-md-3">
                        <div class="card mb-3" style="width: 18rem;">''' in response_data
    

def test_delete_saves_e2e(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/save_build', data = {'build_id': '1'}, follow_redirects=True)
    response = test_app.post('/remove_save', data = {'build_id': '1'},  follow_redirects=True)
    response = test_app.get('/show_saves')
    response_data = response.data.decode('utf-8')
    #page is open, but has nothing
    assert response.status_code == 200
