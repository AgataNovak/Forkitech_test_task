from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_wallet_endpoint():
    response = client.post("/wallet", json={"address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"})
    # TRC20 based USDT smart contract address:TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t с официального сайта TRON
    assert response.status_code == 200
    assert "balance" in response.json()
    assert "bandwidth" in response.json()
    assert "energy" in response.json()
