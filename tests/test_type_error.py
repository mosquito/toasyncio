import unittest
import toasyncio
import tornado.ioloop


class TestTypeError(unittest.TestCase):
    def test_type_error(self):

        @toasyncio.coroutine
        def func():
            yield []

        self.assertRaises(TypeError, tornado.ioloop.IOLoop.current().add_callback(func))

