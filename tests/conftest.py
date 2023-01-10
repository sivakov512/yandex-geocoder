import json
import typing
from urllib.parse import urlencode

import pytest
import requests_mock


@pytest.fixture()
def mock_api() -> typing.Any:
    def _encode(geocode: str, api_key: str = "well-known-key") -> str:
        params = {"format": "json", "apikey": api_key, "geocode": geocode}
        query = urlencode(params)
        return f"https://geocode-maps.yandex.ru/1.x/?{query}"

    with requests_mock.mock() as _m:
        yield lambda resp, status, **encode_kw: _m.get(
            _encode(**encode_kw),
            json=load_fixture(resp) if isinstance(resp, str) else resp,
            status_code=status,
        )


def load_fixture(fixture_name: str) -> dict[str, typing.Any]:
    with open(f"./tests/fixtures/{fixture_name}.json") as fixture:
        return json.load(fixture)  # type: ignore


@pytest.fixture()
def mock_client_response(mocker: typing.Any) -> typing.Any:
    def _mock(fixture_name: str) -> typing.Any:
        with open("./tests/fixtures/{}.json".format(fixture_name)) as fixture:
            return mocker.patch(
                "yandex_geocoder.Client.request",
                return_value=json.load(fixture),
            )

    return _mock
