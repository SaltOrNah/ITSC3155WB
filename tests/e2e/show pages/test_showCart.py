from app import app
from flask.testing import FlaskClient
from repositories import builds_repo

def test_showCart(test_app: FlaskClient):
    response = test_app.get('/cart')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    
def test_add_cart_e2e(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    item = builds_repo.get_part_by_id(1)
    response = test_app.post('/add_to_cart', data = {'part_id': '1'}, follow_redirects=True)
    response = test_app.get('/cart')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert f'''<td>{item['part_type']}</td>''' in response_data

def test_delete_cart_e2e(test_app: FlaskClient):
    response = test_app.post('/signUp', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/login', data = {'username': 'test', 'password': 'password'}, follow_redirects=True)
    response = test_app.post('/add_to_cart', data = {'part_id': '1'}, follow_redirects=True)
    response = test_app.post('/remove_from_cart', data = {'item_id': '1'},  follow_redirects=True)
    response = test_app.get('/cart')
    response_data = response.data.decode('utf-8')
    #page is open, but has nothing
    assert response.status_code == 200
