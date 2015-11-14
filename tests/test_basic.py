# encoding: utf-8
import asyncio
from tornado.gen import sleep
from toasyncio.testing import gen_test, AsyncTestCase


class TestBasic(AsyncTestCase):
    @gen_test
    def test_dummy(self):
        pass

    @gen_test
    def test_basic_func(self):
        print(42)

    @gen_test
    def test_basic_future(self):
        step = 0.1
        count = 10
        t0 = self.io_loop.time()
        for i in range(count):
            yield sleep(step)
        self.assertTrue((t0 + (count * step)) <= self.io_loop.time())

    @gen_test(timeout=10)
    def test_basic_future_gen_timeout(self):
        step = 0.1
        count = 10
        t0 = self.io_loop.time()
        for i in range(count):
            yield sleep(step)

        self.assertTrue((t0 + (count * step)) <= self.io_loop.time())

    @gen_test
    def test_aio_task(self):
        step = 0.1
        count = 10
        t0 = self.io_loop.time()

        for i in range(count):
            yield from asyncio.sleep(step, loop=self.aio_loop)

        self.assertTrue((t0 + (count * step)) <= self.io_loop.time())

    @gen_test
    def test_all_together(self):
        step = 0.1
        count = 10
        t0 = self.io_loop.time()

        for i in range(count):
            yield sleep(step / 2)
            yield from asyncio.sleep(step / 2, loop=self.aio_loop)

        self.assertTrue((t0 + (count * step)) <= self.io_loop.time())
