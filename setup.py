import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author="Nikita Sivakov",
    author_email="sivakov512@gmail.com",
    description=(
        "Simple library for getting address coordinates via Yandex geocoder"
    ),
    install_requires=["requests~=2.20"],
    keywords="yandex geocoder geo coordinates maps api",
    license="MIT",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    name="yandex_geocoder",
    packages=["yandex_geocoder"],
    python_requires=">=3.6",
    url="https://github.com/sivakov512/yandex-geocoder",
    version="1.0.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
