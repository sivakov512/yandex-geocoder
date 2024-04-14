__all__ = ["AsyncClient"]

import dataclasses
import typing
from decimal import Decimal

import aiohttp

from .exceptions import InvalidKey, NothingFound, UnexpectedResponse


@dataclasses.dataclass
class AsyncClient:
    """Yandex geocoder API async client.

    :Example:
        >>> from yandex_geocoder import AsyncClient

        >>> async def main():
        >>>     aclient = AsyncClient(api_key="your-api-key")
        >>>     coordinates = await aclient.coordinates("Москва Льва Толстого 16")
        >>>     assert coordinates == (Decimal("37.587093"), Decimal("55.733974"))
        >>>     address = await aclient.address(Decimal("37.587093"), Decimal("55.733974"))
        >>>     assert address == "Россия, Москва, улица Льва Толстого, 16"
    """

    __slots__ = ("api_key",)

    api_key: str

    async def _request(self, address: str) -> typing.Dict[str, typing.Any]:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get(
                    url="https://geocode-maps.yandex.ru/1.x/",
                    params=dict(format="json", apikey=self.api_key, geocode=address),
            ) as response:
                if response.status == 200:
                    a: typing.Dict[str, typing.Any] = (await response.json())["response"]
                    return a
                elif response.status == 403:
                    raise InvalidKey()
                else:
                    raise UnexpectedResponse(
                        f"status_code={response.status}, body={response.content}"
                    )

    async def coordinates(self, address: str) -> typing.Tuple[Decimal, ...]:
        """Fetch coordinates (longitude, latitude) for passed address."""
        d = await self._request(address)
        data = d["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        coordinates = data[0]["GeoObject"]["Point"]["pos"]
        longitude, latitude = tuple(coordinates.split(" "))
        return Decimal(longitude), Decimal(latitude)

    async def address(self, longitude: Decimal, latitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        response = await self._request(f"{longitude},{latitude}")
        data = response.get("GeoObjectCollection", {}).get("featureMember", [])

        if not data:
            raise NothingFound(f'Nothing found for "{longitude} {latitude}"')

        address_details: str = data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
        return address_details
