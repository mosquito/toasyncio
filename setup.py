# encoding: utf-8
from setuptools import setup, find_packages
import toasyncio

setup(
    name='toasyncio',
    packages=find_packages(exclude=['tests']),
    install_requires=(
        'tornado>=4.2',
        'asyncio',
    ),
    author=toasyncio.__author__,
    version=toasyncio.__version__,
    author_email=", ".join("{email}".format(**a) for a in toasyncio.author_info),
    long_description=open('README.rst', 'r').read(),
    license='MIT',
    keywords=(
        "tornado",
        "asyncio",
    ),
    url='https://github.com/mosquito/toasyncio',
    description='Transparent convert any asyncio futures and inline yield methods to tornado futures.',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)