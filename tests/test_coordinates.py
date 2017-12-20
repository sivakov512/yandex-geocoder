import pytest

from yandex_geocoder import Client
from yandex_geocoder.exceptions import YandexGeocoderAddressNotFound


@pytest.mark.usefixtures('coords_found')
def test_coordinates_found():
    assert Client.coordinates('some address') == ('37.587614', '55.753083')


@pytest.mark.usefixtures('coords_not_found')
def test_coordinates_not_found():
    with pytest.raises(
            YandexGeocoderAddressNotFound, message='"some address" not found'):
        Client.coordinates('some address')
