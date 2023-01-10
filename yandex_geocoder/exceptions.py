__all__ = ["YandexGeocoderException", "UnexpectedResponse", "NothingFound", "InvalidKey"]


class YandexGeocoderException(Exception):
    pass


class UnexpectedResponse(YandexGeocoderException):
    pass


class NothingFound(YandexGeocoderException):
    pass


class InvalidKey(YandexGeocoderException):
    pass
