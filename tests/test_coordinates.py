from decimal import Decimal

import pytest

from yandex_geocoder import (
    Client,
    InvalidKey,
    NothingFound,
    UnexpectedResponse,
)


def test_returns_found_coordinates(mock_api):
    mock_api("coords_found", 200, geocode="Москва Льва Толстого 16")
    client = Client("well-known-key")

    assert client.coordinates("Москва Льва Толстого 16") == (
        Decimal("37.587093"),
        Decimal("55.733969"),
    )


def test_raises_if_coordinates_not_found(mock_api):
    mock_api("coords_not_found", 200, geocode="абырвалг")
    client = Client("well-known-key")

    with pytest.raises(NothingFound, match='Nothing found for "абырвалг"'):
        client.coordinates("абырвалг")


def test_raises_for_invalid_api_key(mock_api):
    mock_api(
        {"statusCode": 403, "error": "Forbidden", "message": "Invalid key"},
        403,
        geocode="Москва Льва Толстого 16",
        api_key="unkown-api-key",
    )
    client = Client("unkown-api-key")

    with pytest.raises(InvalidKey):
        client.coordinates("Москва Льва Толстого 16")


def test_raises_for_unknown_response(mock_api):
    mock_api({}, 500, geocode="Москва Льва Толстого 16")
    client = Client("well-known-key")

    with pytest.raises(UnexpectedResponse) as exc_info:
        client.coordinates("Москва Льва Толстого 16")

    assert "status_code=500, body=b'{}'" in exc_info.value.args
