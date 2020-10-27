import requests
def test_show_clients(app):
    response = requests.get("http://localhost:5000/clientes")
    assert response.status_code == 200

def test_show_clients_json(app):
    response = requests.get("http://localhost:5000/clientes")
    assert response.headers["Content-Type"] == "application/json"

def test_get_client(app):
    response = requests.get("http://localhost:5000/clientes/1")
    assert response.status_code == 200

def test_get_client_json(app):
    response = requests.get("http://localhost:5000/clientes/1")
    assert response.headers["Content-Type"] == "application/json"
