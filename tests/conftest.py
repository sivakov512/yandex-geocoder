import json

import pytest
import requests_mock


@pytest.fixture
def mock_response():
    with requests_mock.mock() as _m:
        yield lambda **kwargs: _m.get(
            "https://geocode-maps.yandex.ru/1.x/?geocode=b&format=json", **kwargs
        )


@pytest.fixture
def mock_client_response(mocker):
    def _mock(fixture_name):
        with open("./tests/fixtures/{}.json".format(fixture_name)) as fixture:
            return mocker.patch(
                "yandex_geocoder.Client.request", return_value=json.load(fixture),
            )

    return _mock
