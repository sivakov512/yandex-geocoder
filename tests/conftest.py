import pytest
import requests_mock


@pytest.fixture
def requests_mocker() -> requests_mock.Mocker:
    mocker = requests_mock.Mocker()
    mocker.start()

    yield mocker

    mocker.stop()
