import pytest

from yandex_geocoder import (
    Client,
    InvalidKey,
    NothingFound,
    UnexpectedResponse,
)


def test_returns_found_coordinates(mock_api):
    mock_api("coords_found", 200, geocode="some address")
    client = Client("123456")

    assert client.coordinates("some address") == ("37.587614", "55.753083")


def test_raises_if_coordinates_not_found(mock_api):
    mock_api("coords_not_found", 200, geocode="unknown address")
    client = Client("123456")

    with pytest.raises(NothingFound, match='Nothing found for "unknown address"'):
        client.coordinates("unknown address")


def test_raises_for_invalid_api_key(mock_api):
    mock_api(
        {"statusCode": 403, "error": "Forbidden", "message": "Invalid key"},
        403,
        geocode="some address",
        api_key="unkown-api-key",
    )
    client = Client("unkown-api-key")

    with pytest.raises(InvalidKey):
        client.coordinates("some address")


def test_raises_for_unknown_response(mock_api):
    mock_api({}, 500, geocode="some address")
    client = Client("123456")

    with pytest.raises(UnexpectedResponse) as exc_info:
        client.coordinates("some address")

    assert "status_code=500, body=b'{}'" in exc_info.value.args
