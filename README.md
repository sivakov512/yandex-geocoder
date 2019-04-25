Yandex Geocoder
===
Get address coordinates via Yandex geocoder

[![Build Status](https://travis-ci.org/sivakov512/yandex-geocoder.svg?branch=master)](https://travis-ci.org/sivakov512/yandex-geocoder)
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

``` python
from yandex_geocoder import Client
Client.coordinates('Хабаровск 60 октября 150')  # ('135.114326', '48.47839')
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

Credits
---
- [f213](https://github.com/f213)
