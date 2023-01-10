__all__ = ["Client"]

import dataclasses
import typing
from decimal import Decimal

import requests

from .exceptions import InvalidKey, NothingFound, UnexpectedResponse


@dataclasses.dataclass
class Client:
    """Yandex geocoder API client.

    :Example:
        >>> from yandex_geocoder import Client
        >>> client = Client("your-api-key")

        >>> coordinates = client.coordinates("Москва Льва Толстого 16")
        >>> assert coordinates == (Decimal("37.587093"), Decimal("55.733969"))

        >>> address = client.address(Decimal("37.587093"), Decimal("55.733969"))
        >>> assert address == "Россия, Москва, улица Льва Толстого, 16"

    """

    __slots__ = ("api_key",)

    api_key: str

    def _request(self, address: str) -> dict[str, typing.Any]:
        response = requests.get(
            "https://geocode-maps.yandex.ru/1.x/",
            params=dict(format="json", apikey=self.api_key, geocode=address),
        )

        if response.status_code == 200:
            got: dict[str, typing.Any] = response.json()["response"]
            return got
        elif response.status_code == 403:
            raise InvalidKey()
        else:
            raise UnexpectedResponse(
                f"status_code={response.status_code}, body={response.content!r}"
            )

    def coordinates(self, address: str) -> tuple[Decimal, ...]:
        """Fetch coordinates (longitude, latitude) for passed address."""
        data = self._request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        coordinates: str = data[0]["GeoObject"]["Point"]["pos"]
        longitude, latitude = tuple(coordinates.split(" "))

        return Decimal(longitude), Decimal(latitude)

    def address(self, longitude: Decimal, latitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        data = self._request(f"{longitude},{latitude}")["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{longitude} {latitude}"')

        got: str = data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
        return got
