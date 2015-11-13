toasyncio
=========

.. image:: https://travis-ci.org/mosquito/toasyncio.svg
    :target: https://travis-ci.org/mosquito/toasyncio

.. image:: https://img.shields.io/pypi/v/toasyncio.svg
    :target: https://pypi.python.org/pypi/toasyncio/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/toasyncio.svg
    :target: https://pypi.python.org/pypi/toasyncio/

.. image:: https://img.shields.io/pypi/pyversions/toasyncio.svg
    :target: https://pypi.python.org/pypi/toasyncio/

.. image:: https://img.shields.io/pypi/l/toasyncio.svg
    :target: https://pypi.python.org/pypi/toasyncio/

Write on tornado with asyncio easy.

About
=====

Transparent convert any asyncio futures and inline yield methods to tornado futures.

Examples
========

Using

::

    import tornado.gen
    import asyncio
    from tornado.ioloop import IOLoop
    from toasyncio.gen import coroutine

    @coroutine
    def test():
        print('Tornado future')
        yield tornago.gen.sleep(1)
        print('Asyncio future')
        yield from asyncio.sleep(1, loop=IOLoop.current().asyncio_loop)
        print('Done')

    IOLoop.current().run_sync(test)


Testing

::

    import asyncio
    from tornado.gen import sleep
    from toasyncio.testing import gen_test, AsyncTestCase


    class TestBasic(AsyncTestCase):
        @gen_test
        def test_all_together(self):
            step = 0.1
            count = 10
            t0 = self.io_loop.time()

            for i in range(count):
                yield sleep(step / 2)
                yield from asyncio.sleep(step / 2, loop=self.aio_loop)

            self.assertTrue((t0 + (count * step)) <= self.io_loop.time())
