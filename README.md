Yandex Geocoder
===
Get address coordinates via Yandex geocoder

Code is impudently stolen from [f213](https://github.com/f213).

[![Build Status](https://travis-ci.org/cryptomaniac512/yandex-geocoder.svg?branch=master)](https://travis-ci.org/cryptomaniac512/yandex-geocoder)
[![Coverage Status](https://coveralls.io/repos/github/cryptomaniac512/yandex-geocoder/badge.svg?branch=master)](https://coveralls.io/github/cryptomaniac512/yandex-geocoder?branch=master)
![Python versions](https://img.shields.io/badge/python-3.5,%203.6-blue.svg)

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

