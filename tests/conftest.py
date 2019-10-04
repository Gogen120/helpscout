import os

import pytest

from helpscout.helpscout import Client

APP_ID = os.getenv("TEST_APP_ID")
APP_SECRET = os.getenv("TEST_APP_SECRET")


@pytest.fixture
def test_client():
    return Client(APP_ID, APP_SECRET)


@pytest.fixture
def test_client_with_invalid_credentials():
    return Client("", "")
