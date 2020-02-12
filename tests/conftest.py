import json
from urllib.parse import urlencode

import pytest
import requests_mock


@pytest.fixture
def mock_api():
    def _encode(geocode: str, api_key: str = "123456") -> str:
        params = {"format": "json", "apikey": api_key, "geocode": geocode}
        query = urlencode(params)
        return f"https://geocode-maps.yandex.ru/1.x/?{query}"

    with requests_mock.mock() as _m:
        yield lambda resp, status, **encode_kw: _m.get(
            _encode(**encode_kw),
            json=load_fixture(resp) if isinstance(resp, str) else resp,
            status_code=status,
        )


def load_fixture(fixture_name: str) -> dict:
    with open(f"./tests/fixtures/{fixture_name}.json") as fixture:
        return json.load(fixture)


@pytest.fixture
def mock_client_response(mocker):
    def _mock(fixture_name):
        with open("./tests/fixtures/{}.json".format(fixture_name)) as fixture:
            return mocker.patch(
                "yandex_geocoder.Client.request", return_value=json.load(fixture),
            )

    return _mock
