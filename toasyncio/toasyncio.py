import types
import asyncio
import tornado.ioloop
import tornado.gen
import tornado.platform.asyncio


def coroutine(func):
    @tornado.gen.coroutine
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, types.GeneratorType):
            return result

        io_loop = tornado.ioloop.IOLoop.current()

        current_future = None
        current_result = None

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
                    raise TypeError('Expected generator or future: %s' % type(current_future))

                current_future = result.send(current_result)

        except StopIteration as e:
            return e.value

        return current_result

    return wrap

