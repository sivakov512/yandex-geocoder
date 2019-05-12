import typing

import requests

from yandex_geocoder.exceptions import (
    YandexGeocoderAddressNotFound,
    YandexGeocoderHttpException,
    YandexGeocodeLocationNotFound
)


class Client:
    """Yandex geocoder API client.

    :Example:
        >>> from yandex_geocoder import Client
        >>> Client.coordinates('Хабаровск 60 октября 150')
        ('135.114326', '48.47839')
        >>> from yandex_geocoder.client import Client
        >>> Client.location(longitude='69.279737', latitude='41.311151')
        Узбекистан, Ташкент, сквер Амира Темура

    """

    API_URL = "https://geocode-maps.yandex.ru/1.x/"
    PARAMS = {"format": "json"}

    @classmethod
    def request(cls, address=None, longitude=None, latitude=None) -> dict:
        """Requests passed address and returns content of `response` key.

        Raises `YandexGeocoderHttpException` if response's status code is
        different from `200`.

        """
        if address is not None:
            response = requests.get(
                cls.API_URL, params=dict(geocode=address, **cls.PARAMS)
            )

            if response.status_code != 200:
                raise YandexGeocoderHttpException(
                    "Non-200 response from yandex geocoder"
                )

            return response.json()["response"]
        else:
            location = '{},{}'.format(longitude, latitude)
            response = requests.get(
                cls.API_URL, params=dict(geocode=location, **cls.PARAMS)
            )
            if response.status_code != 200:
                raise YandexGeocoderHttpException(
                    "Non-200 response from yandex geocoder"
                )

            return response.json()["response"]

    @classmethod
    def coordinates(cls, address: str) -> typing.Tuple[str, str]:
        """Returns a tuple of ccordinates (longtitude, latitude) for
        passed address.

        Raises `YandexGeocoderAddressNotFound` if nothing found.

        """
        data = cls.request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise YandexGeocoderAddressNotFound(
                '"{}" not found'.format(address)
            )

        coordinates = data[0]["GeoObject"]["Point"]["pos"]  # type: str
        return tuple(coordinates.split(" "))

    @classmethod
    def location(cls, longitude, latitude):

        data = cls.request(longitude=longitude, latitude=latitude)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise YandexGeocodeLocationNotFound(
                '"{},{}" not found'.format(longitude, latitude)
            )
        location = data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
        return location

