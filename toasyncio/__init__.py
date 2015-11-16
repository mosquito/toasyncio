# encoding: utf-8

version_info = (0, 5, 1)
author_info = (
    {"name": "Ilya Smirnov", "email": "ilya94@mail.ru"},
    {"name": "Dmitry Orlov", "email": "me@mosquito.su"},
)

__version__ = ".".join(map(str, version_info))
__author__ = ", ".join("{name} <{email}>".format(**a) for a in author_info)

