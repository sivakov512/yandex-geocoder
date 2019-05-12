class YandexGeocoderException(Exception):
    pass


class YandexGeocoderHttpException(YandexGeocoderException):
    pass


class YandexGeocoderAddressNotFound(YandexGeocoderException):
    pass

class YandexGeocodeLocationNotFound(YandexGeocoderException):
    pass