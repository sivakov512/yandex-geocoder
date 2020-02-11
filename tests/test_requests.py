import pytest

from yandex_geocoder import Client
from yandex_geocoder.exceptions import YandexGeocoderHttpException


def test_request_ok(mock_response):
    mock_response(json={"response": {"ok": True}})

    assert Client.request("b") == {"ok": True}


def test_request_fails(mock_response):
    mock_response(status_code=400)

    with pytest.raises(
        YandexGeocoderHttpException, match="Non-200 response from yandex geocoder",
    ):
        Client.request("b")
