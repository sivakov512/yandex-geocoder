from setuptools import setup

setup(
    author='Nikita Sivakov',
    author_email='sivakov512@gmail.com',
    description=(
        'Simple library for getting address coordinates via Yandex geocoder'),
    install_requires=[
        'requests~=2.20',
    ],
    keywords='yandex geocoder geo coordinates maps api',
    license='MIT',
    long_description_markdown_filename='README.md',
    name='yandex_geocoder',
    packages=['yandex_geocoder'],
    python_requires='>=3.5',
    setup_requires=['setuptools-markdown'],
    url='https://github.com/sivakov512/yandex-geocoder',
    version='0.1.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
