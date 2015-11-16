# encoding: utf-8
import types
import asyncio
import tornado.ioloop
import tornado.gen
import tornado.platform.asyncio
import traceback
from functools import wraps


def coroutine(func):
    @tornado.gen.coroutine
    @wraps(func)
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, types.GeneratorType):
            return result

        io_loop = tornado.ioloop.IOLoop.current()

        assert isinstance(io_loop, tornado.platform.asyncio.AsyncIOLoop), \
            "IOLoop must be instance of tornado.platform.asyncio.AsyncIOLoop"

        current_future = None

        try:
            while True:
                if not current_future:
                    current_future = next(result)

                if isinstance(current_future, (tornado.gen.Future, list)):
                    current_result = yield current_future

                elif isinstance(current_future, types.GeneratorType):
                    task = asyncio.tasks.Task(current_future, loop=io_loop.asyncio_loop)
                    current_result = yield tornado.platform.asyncio.to_tornado_future(task)

                elif isinstance(current_future, asyncio.Future):
                    current_result = yield tornado.platform.asyncio.to_tornado_future(current_future)

                else:
                    result.throw(TypeError, 'Expected generator or future: %s' % type(current_future),
                                 result.gi_frame.f_trace)

                current_future = result.send(current_result)

        except StopIteration as e:
            return e.value

    return wrap


tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
