from flask.testing import FlaskClient

def test_index(test_app: FlaskClient):
    response = test_app.get('/')
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '''<header>
        <h1 style="color: #333; font-size: 48px; text-shadow: 2px 2px 4px #aaa;">Welcome to 
            <span style="color: #FF4500;">Parts Complier''' in response_data