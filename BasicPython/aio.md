```python
py3 官方逻辑
import asyncio


@asyncio.coroutine
def test():
    a = yield from test2()
    import traceback
    traceback.print_stack()
    print(a)


@asyncio.coroutine
def test2():
    a = yield from test3()
    yield from asyncio.sleep(5)
    return a + 1


@asyncio.coroutine
def test3():
    yield from asyncio.sleep(5)
    return 1


asyncio.run(test())
```



```python
我自己实现的核心思想的逻辑

class Future():
    def __init__(self) -> None:
        self._is_done = False
        self.data = None
        self.func = None

    def set_result(self, data):
        print('set_result', data)
        self._result = data
        self._is_done = True

    def is_done(self):
        return self._is_done

    def result(self):
        return self._result
    
    def __await__(self):
        if not self.is_done():
            self._asyncio_future_blocking = True
            yield self  # This tells Task to wait for completion.
        if not self.is_done():
            raise RuntimeError("await wasn't used with future")
        print('aaaa', self.result())
        return self.result()  # May raise too.

    __iter__ = __await__  # make compatible with 'yield from'.



# @ coroutine
def test():
    a = yield from test2()
    print('result>>', a)


# @ coroutine
def test2():
    a = yield from asyncio_sleep(2)
    return a + 1


# @ coroutine
def asyncio_sleep(sec):
    f = Future()
    result = yield from f
    return result

    
def main():
    a = test()
    # 在官方逻辑，coroutine装饰器的函数会被包装成Task执行，
    # Task的Handle函数核心逻辑就是调用send获取到future对象
    # 然后把Task对象的wakeup函数注册到future对象回调函数
    f = a.send(None)	
    print('?>>>', f)	# f是一个future对象
    # f 获得结果，触发Task的wakeup函数
    f.set_result(1)
    # 然后执行一次Task的Handle函数
    # 这时候重新执行一次send，future会返回结果，然后继续走函数的yield的后续流程
    a.send(None)

main()


```

