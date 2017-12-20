import requests

from yamaps_coords.exceptions import YamapsCoordsHttpException


class Client:

    API_URL = 'https://geocode-maps.yandex.ru/1.x/'
    PARAMS = {'format': 'json'}

    def request(self, address: str) -> dict:
        response = requests.get(self.API_URL, params=dict(
            geocode=address, **self.PARAMS))

        if response.status_code != 200:
            raise YamapsCoordsHttpException(
                'Non-200 response from yandex geocoder')

        return response.json()['response']
