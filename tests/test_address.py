from decimal import Decimal

import pytest

from yandex_geocoder import (
    Client,
    InvalidKey,
    NothingFound,
    UnexpectedResponse,
)


def test_returns_found_address(mock_api):
    mock_api("address_found", 200, geocode="37.587093,55.733969")
    client = Client("well-known-key")

    assert (
        client.address(Decimal("37.587093"), Decimal("55.733969"))
        == "Россия, Москва, улица Льва Толстого, 16"
    )


def test_raises_if_address_not_found(mock_api):
    mock_api("address_not_found", 200, geocode="337.587093,55.733969")
    client = Client("well-known-key")

    with pytest.raises(NothingFound, match='Nothing found for "337.587093 55.733969"'):
        client.address(Decimal("337.587093"), Decimal("55.733969"))


def test_raises_for_invalid_api_key(mock_api):
    mock_api(
        {"statusCode": 403, "error": "Forbidden", "message": "Invalid key"},
        403,
        geocode="37.587093,55.733969",
        api_key="unkown-api-key",
    )
    client = Client("unkown-api-key")

    with pytest.raises(InvalidKey):
        client.address(Decimal("37.587093"), Decimal("55.733969"))


def test_raises_for_unknown_response(mock_api):
    mock_api({}, 500, geocode="37.587093,55.733969")
    client = Client("well-known-key")

    with pytest.raises(UnexpectedResponse) as exc_info:
        client.address(Decimal("37.587093"), Decimal("55.733969"))

    assert "status_code=500, body=b'{}'" in exc_info.value.args
