Yandex Geocoder
===
Get address coordinates via Yandex geocoder

[![Build Status](https://github.com/sivakov512/yandex-geocoder/workflows/test/badge.svg)](https://github.com/sivakov512/yandex-geocoder/actions?query=workflow%3Atest)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/yandex-geocoder/badge.svg?branch=master)](https://coveralls.io/github/sivakov512/yandex-geocoder?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python versions](https://img.shields.io/pypi/pyversions/yandex-geocoder.svg)](https://pypi.python.org/pypi/yandex-geocoder)
[![PyPi](https://img.shields.io/pypi/v/yandex-geocoder.svg)](https://pypi.python.org/pypi/yandex-geocoder)

Installation
---
Install it via `pip` tool:

``` shell
pip install yandex-geocoder
```

Usage example
---
Yandex Geocoder requires an API developer key, you can get it [here](https://developer.tech.yandex.ru/services/) to use this library.

``` python
from decimal import Decimal

from yandex_geocoder import Client


client = Client("your-api-key")

coordinates = client.coordinates("Москва Льва Толстого 16")
assert coordinates == (Decimal("37.587093"), Decimal("55.733969"))

address = client.address(Decimal("37.587093"), Decimal("55.733969"))
assert address == "Россия, Москва, улица Льва Толстого, 16"
```

Development and contribution
---

* install project dependencies
```bash
python setup.py develop
```

* install linting, formatting and testing tools
```bash
pip install -r requirements.txt
```

* run tests
```bash
pytest
```

* run linters
```bash
flake8
black --check ./
```

* feel free to contribute!
