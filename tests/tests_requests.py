import pytest

from yamaps_coords import Client
from yamaps_coords.exceptions import YamapsCoordsHttpException


def test_request_ok(requests_mocker):
    requests_mocker.get(
        'https://geocode-maps.yandex.ru/1.x/?geocode=b&format=json',
        json={'response': {'ok': True}})

    assert Client().request('b') == {'ok': True}


def test_request_fails(requests_mocker):
    requests_mocker.get(
        'https://geocode-maps.yandex.ru/1.x/?geocode=b&format=json',
        status_code=400)

    with pytest.raises(
            YamapsCoordsHttpException,
            message='Non-200 response from yandex geocoder'):
        Client().request('b')
