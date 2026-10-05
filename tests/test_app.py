import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app("development")
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json
    assert "Health check OK" in response.get_data(as_text=True)


def test_root_returns_app_info(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Root endpoint" in response.get_data(as_text=True)


def test_status_reports_uptime(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert "uptime_seconds" in response.get_data(as_text=True)


def test_unknown_route_returns_404(client):
    assert client.get("/does-not-exist").status_code == 404


def test_post_to_health_not_allowed(client):
    assert client.post("/health").status_code == 405