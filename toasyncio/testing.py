# encoding: utf-8
from .gen import coroutine
from tornado.ioloop import IOLoop
import tornado.testing
import tornado.platform.asyncio
from functools import wraps, partial


def gen_test(func=None, timeout=None):
    if timeout is None:
        timeout = tornado.testing.get_async_test_timeout()

    def wrap(f):
        @wraps(f)
        def pre_coroutine(self, *args, **kwargs):
            result = f(self, *args, **kwargs)

            is_coroutine = any((
                isinstance(result, tornado.testing.GeneratorType),
                tornado.testing.iscoroutine(result)
            ))

            self._test_generator = result if is_coroutine else None
            return result

        if tornado.testing.iscoroutinefunction(f):
            coro = pre_coroutine
        else:
            coro = coroutine(pre_coroutine)

        @wraps(coro)
        def post_coroutine(self, *args, **kwargs):
            io_loop = getattr(self, "io_loop", None)
            io_loop = io_loop or IOLoop.instance()
            try:
                p = partial(coro, self, *args, **kwargs)
                assert isinstance(io_loop, tornado.platform.asyncio.AsyncIOLoop), \
                    "IOLoop must be instance of tornado.platform.asyncio.AsyncIOLoop"
                return self.io_loop.run_sync(p, timeout=timeout)
            except TimeoutError as e:
                self._test_generator.throw(e)
                raise

        return post_coroutine

    if func is not None:
        return wrap(func)
    else:
        return wrap


class _AIOPropMixin:
    @property
    def aio_loop(self):
        return self.io_loop.asyncio_loop


class AsyncTestCase(_AIOPropMixin, tornado.testing.AsyncTestCase):
    pass


class AsyncHTTPTestCase(_AIOPropMixin, tornado.testing.AsyncHTTPTestCase):
    pass
