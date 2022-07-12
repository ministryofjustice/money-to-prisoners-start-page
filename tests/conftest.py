import pytest


@pytest.fixture()
def app():
    from app import app

    return app


@pytest.fixture()
def settings():
    from app import settings

    return settings


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
