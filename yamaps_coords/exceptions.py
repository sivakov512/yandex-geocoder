class YamapsCoordsException(Exception):
    pass


class YamapsCoordsHttpException(YamapsCoordsException):
    pass


class YamapsCoordsAddressNotFound(YamapsCoordsException):
    pass
