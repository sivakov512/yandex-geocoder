import pytest

from yandex_geocoder import Client
from yandex_geocoder.exceptions import YandexGeocoderHttpException


def test_request_ok(requests_mocker):
    requests_mocker.get(
        "https://geocode-maps.yandex.ru/1.x/?geocode=b&format=json",
        json={"response": {"ok": True}},
    )

    assert Client.request("b") == {"ok": True}


def test_request_fails(requests_mocker):
    requests_mocker.get(
        "https://geocode-maps.yandex.ru/1.x/?geocode=b&format=json",
        status_code=400,
    )

    with pytest.raises(
        YandexGeocoderHttpException,
        match="Non-200 response from yandex geocoder",
    ):
        Client.request("b")
