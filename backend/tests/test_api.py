from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

def test_calculate_addition():
    response = client.post(
        "/calculate",
         json={"expression": "2+3"})

    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_calculate_parentheses():
    response = client.post(
        "/calculate",
        json={"expression": "(2+3)*4"},
    )

    assert response.status_code == 200
    assert response.json() == {"result": 20.0}


def test_calculate_power():
    response = client.post(
        "/calculate",
        json={"expression": "2^3"},
    )

    assert response.status_code == 200
    assert response.json() == {"result": 8.0}


def test_calculate_function():
    response = client.post(
        "/calculate",
        json={"expression": "sqrt(9)"},
    )

    assert response.status_code == 200
    assert response.json() == {"result": 3.0}


def test_invalid_expression():
    response = client.post(
        "/calculate",
        json={"expression": "2+"},
    )

    assert response.status_code == 500
