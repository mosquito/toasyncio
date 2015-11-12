import unittest
import toasyncio
import tornado.gen
import tornado.ioloop
import asyncio


class TestRaw(unittest.TestCase):
    def test_just_func(self):

        def raw_func():
            return True

        self.assertEqual(type(tornado.gen.coroutine(raw_func)()), type(toasyncio.coroutine(raw_func)()))

    def test_raw_tornado(self):

        @tornado.gen.coroutine
        def raw_func():
            return True

        self.assertEqual(type(tornado.gen.coroutine(raw_func)()), type(toasyncio.coroutine(raw_func)()))

    def test_raw_asyncio(self):

        @asyncio.coroutine
        def raw_func():
            return True

        self.assertEqual(True, tornado.ioloop)