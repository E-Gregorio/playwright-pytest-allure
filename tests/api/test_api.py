import requests

def test_get_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    
    # Validar la estructura de la respuesta
    data = response.json()
    assert 'id' in data
    assert 'title' in data