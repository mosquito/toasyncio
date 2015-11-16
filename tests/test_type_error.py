# encoding: utf-8
from toasyncio.testing import gen_test, AsyncTestCase
from tornado.stack_context import wrap
from toasyncio.gen import coroutine


class TestTypeError(AsyncTestCase):
    @gen_test
    def test_type_error(self):
        try:
            yield tuple()
        except TypeError:
            pass
        else:
            self.fail('TypeError not raised')

