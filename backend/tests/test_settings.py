from app import main

def test_settings(test_app):
    response = test_app.get("/settings")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "testing": True}