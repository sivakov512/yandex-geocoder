import pytest

from yandex_geocoder import Client
from yandex_geocoder.exceptions import YandexGeocoderAddressNotFound


def test_returns_found_coordinates(mock_client_response):
    mock_client_response("coords_found")

    assert Client.coordinates("some address") == ("37.587614", "55.753083")


def test_raises_if_coordinates_not_found(mock_client_response):
    mock_client_response("coords_not_found")

    with pytest.raises(YandexGeocoderAddressNotFound, match='"some address" not found'):
        Client.coordinates("some address")
