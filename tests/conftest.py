import json
import typing

import pytest
import requests_mock


@pytest.fixture
def requests_mocker():
    mocker = requests_mock.Mocker()
    mocker.start()

    yield mocker

    mocker.stop()


def load_fixture(name: str) -> typing.Union[dict, list]:
    with open("./tests/fixtures/{}.json".format(name)) as fixture:
        return json.load(fixture)


@pytest.fixture
def coords_found(mocker):
    fixture = load_fixture("coords_found")
    return mocker.patch("yandex_geocoder.Client.request", return_value=fixture)


@pytest.fixture
def coords_not_found(mocker):
    fixture = load_fixture("coords_not_found")
    return mocker.patch("yandex_geocoder.Client.request", return_value=fixture)
