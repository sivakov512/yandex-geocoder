import typing

import requests

from yandex_geocoder.exceptions import (
    YandexGeocoderAddressNotFound, YandexGeocoderHttpException)


class Client:

    API_URL = 'https://geocode-maps.yandex.ru/1.x/'
    PARAMS = {'format': 'json'}

    @classmethod
    def request(cls, address: str) -> dict:
        response = requests.get(cls.API_URL, params=dict(
            geocode=address, **cls.PARAMS))

        if response.status_code != 200:
            raise YandexGeocoderHttpException(
                'Non-200 response from yandex geocoder')

        return response.json()['response']

    @classmethod
    def coordinates(cls, address: str) -> typing.Tuple[str, str]:
        data = cls.request(address)['GeoObjectCollection']['featureMember']

        if not data:
            raise YandexGeocoderAddressNotFound(
                '"{}" not found'.format(address))

        coordinates = data[0]['GeoObject']['Point']['pos']  # type: str
        return tuple(coordinates.split(' '))
