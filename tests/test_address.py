import typing
from decimal import Decimal

import pytest

from yandex_geocoder import AsyncClient, Client, InvalidKey, NothingFound, UnexpectedResponse


def test_returns_found_address(mock_api: typing.Any) -> None:
    mock_api("address_found", 200, geocode="37.587093,55.733969")
    client = Client("well-known-key")

    assert (
        client.address(Decimal("37.587093"), Decimal("55.733969"))
        == "Россия, Москва, улица Льва Толстого, 16"
    )


@pytest.mark.asyncio
async def test_returns_found_address_async(async_mock_api: typing.Any) -> None:
    async_mock_api("address_found", 200, geocode="37.587093,55.733969")
    client = AsyncClient("well-known-key")

    resp = await client.address(Decimal("37.587093"), Decimal("55.733969"))
    assert resp == "Россия, Москва, улица Льва Толстого, 16"


def test_raises_if_address_not_found(mock_api: typing.Any) -> None:
    mock_api("address_not_found", 200, geocode="337.587093,55.733969")
    client = Client("well-known-key")

    with pytest.raises(NothingFound, match='Nothing found for "337.587093 55.733969"'):
        client.address(Decimal("337.587093"), Decimal("55.733969"))


@pytest.mark.asyncio
async def test_raises_if_address_not_found_async(async_mock_api: typing.Any) -> None:
    async_mock_api("address_not_found", 200, geocode="337.587093,55.733969")
    client = AsyncClient("well-known-key")

    with pytest.raises(NothingFound, match='Nothing found for "337.587093 55.733969"'):
        await client.address(Decimal("337.587093"), Decimal("55.733969"))


def test_raises_for_invalid_api_key(mock_api: typing.Any) -> None:
    mock_api(
        {"statusCode": 403, "error": "Forbidden", "message": "Invalid key"},
        403,
        geocode="37.587093,55.733969",
        api_key="unkown-api-key",
    )
    client = Client("unkown-api-key")

    with pytest.raises(InvalidKey):
        client.address(Decimal("37.587093"), Decimal("55.733969"))


@pytest.mark.asyncio
async def test_raises_for_invalid_api_key_async(async_mock_api: typing.Any) -> None:
    async_mock_api(
        {"statusCode": 403, "error": "Forbidden", "message": "Invalid key"},
        403,
        geocode="37.587093,55.733969",
        api_key="unkown-api-key",
    )
    client = AsyncClient("unkown-api-key")

    with pytest.raises(InvalidKey):
        await client.address(Decimal("37.587093"), Decimal("55.733969"))


def test_raises_for_unknown_response(mock_api: typing.Any) -> None:
    mock_api({}, 500, geocode="37.587093,55.733969")
    client = Client("well-known-key")

    with pytest.raises(UnexpectedResponse) as exc_info:
        client.address(Decimal("37.587093"), Decimal("55.733969"))

    assert "status_code=500, body=b'{}'" in exc_info.value.args


@pytest.mark.asyncio
async def test_raises_for_unknown_response_async(async_mock_api: typing.Any) -> None:
    async_mock_api({}, 500, geocode="37.587093,55.733969")
    client = AsyncClient("well-known-key")

    with pytest.raises(UnexpectedResponse) as exc_info:
        await client.address(Decimal("37.587093"), Decimal("55.733969"))

    assert "status_code=500, body=b'{}'" in exc_info.value.args
