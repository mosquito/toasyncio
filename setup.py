# encoding: utf-8
from setuptools import setup

setup(
    name='toasyncio',
    version='0.1',
    packages=['toasyncio'],
    install_requires=[
        'tornado>=4.2',
    ],
    author='Ilya Smirnov',
    author_email='ilya94@mail.ru',
    url='https://github.com/mosquito/mytor',
    license='MIT',
    keywords=[
        "tornado", "asyncio"
    ],
    description='Coroutine wrapper from asyncio to tornado.',
    zip_safe=False,
)