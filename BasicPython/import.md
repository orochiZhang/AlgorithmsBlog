# Python import机制

## package 和 module 概念
1. module 可以是一个py文件，一个pyd文件，dll文件，一个so文件。   
2. package必须是一个文件夹，并且文件夹里面必须有\_\_init__.py文件。
3. import 文件夹A，实际上是把<module 'A' from 'D:\\python Code\\A\\\_\_init__.py'>动态加载到sys.modules。

## 关于import
### 当你执行一个import操作
1. python虚拟机把module A动态加载到sys.modules
2. python虚拟机引入符号'A',
3. 把'A'映射到sys.modules的module A
4. 把'A'加入到当前名字空间
```python
>>> import A
>>> dir()
['A','__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__' ]
```

但是，import A.test，为什么当前名字空间没有A.test?   
1. python虚拟机把module A动态加载到sys.modules
2. 在module A的__path__搜索module test
3. python虚拟机把module A.test动态加载到sys.modules
4. python虚拟机引入符号'A',
5. 把'A'映射到sys.modules的module A
6. 把'A'加入到当前名字空间
```python
>>> import A.test
>>> dir()
['A', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```
为什么是A.test?这是为了让A.test和B.test在sys.modules里面和平共存。

### 当你执行一个import as操作
1. python虚拟机把A.test动态加载到sys.modules
2. python虚拟机引入符号't',
3. 把't'映射到sys.modules的module A.test
4. 把't'加入到当前名字空间
```python
>>> import A.test as t
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 't']
```

### 所有的import的模块都会在sys.module缓存。 
举个例子：   
test3.py
```python
B = 4
```
del test3，不能调用test3.B。但是sys.module仍然存在test3。
```python
import sys
import test3

print(sys.modules['test3'])
print(test3.B)
del test3
print(sys.modules['test3'])
print(test3.B)
```
输出:
```python
<module 'test3' from 'D:\\python Code\\test3.py'>
4
<module 'test3' from 'D:\\python Code\\test3.py'>
NameError: name 'test3' is not defined
```

### from import 和 import
举个例子：
A/test.py
```python
B = 3
```
命令行执行：
```python
>>> from A.test import B
>>> dir()
['B', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import sys
>>> print(sys.modules['A'])
<module 'A' from 'D:\\python Code\\A\\__init__.py'>
>>> print(sys.modules['A.test'])
<module 'A.test' from 'D:\\python Code\\A\\test.py'>
```
from import 和import没有本质区别，都是要把A, A.test 加载到sys.modules。    
区别是from import 会把符号'B'加入到当前名字空间，但没有把符号'A'加入到当前名字空间。


## 关于reload
importlib.reload 只会更新模块修改了的对象和新增的对象。
源码文件删除了的对象，reload后依然存在。

1. test.py文件内容
```python
class A():
     pass
```
2. 命令行执行：
```python
>>>import test
>>>print(test.A)
<class 'test.A'>
```
3. test.py修改后
```python
B = 1
```
4. 命令行执行：
```python
>>>import importlib
>>>importlib.reload(test)
>>>test.B
1
>>>test.A
<class 'test.A'>
```

## 关于import和reload
所有的import动作，第一次都会在sys.module缓存。   
第二次之后的import都是使用sys.module缓存。   
reload相当于重新执行一次import。   

test1.py
```python
import test3

class A():
	pass
```
test2.py
```python
import test3
print('first:', test3.B)
test3.B = 1
print('change:', test3.B)
import test1
# from test1 import A
print('import test1:',test3.B)
import importlib
importlib.reload(test3)
print('reload:', test3.B)
```
test3.py
```python
B = 4
print('hello')
```
执行test2.py的结果
```python
hello
first: 4
change: 1
import test1: 1
hello
reload: 4
```

### 避免全局变量在reload中被替换
把test3.py改成如下,即可避免B在reload的时候还原。
```python
if 'B' not in globals():
	B = 4
print('hello')
```

## 循环import的问题与解决方案
举个例子:   
test1.py
```python
import test2

class A():
	def __init__(self):
		test2.test()

a = A()
```
test2.py
```python
import test1

def test():
	print(test1.A)
```
如果执行test1.py,运行顺序如下报错所示：
```python
Traceback (most recent call last):
  File "D:/python Code/test1.py", line 2, in <module>
    import test2
  File "D:\python Code\test2.py", line 2, in <module>
    import test1
  File "D:\python Code\test1.py", line 8, in <module>
    a = A()
  File "D:\python Code\test1.py", line 6, in __init__
    test2.test()
AttributeError: module 'test2' has no attribute 'test'
```
因为test2.py里面import了test1.py,所以又继续test1.py的初始化。     
执行到``a = A()``的时候，test2.py还没初始化完，所以没有test函数。

解决方案：
1. 如果是脚本执行，在test1.py改为如下即可:
```python
if __name__ == '__main__':
	a = A()
```
``__name__``是python的一个内置类属性，它存储模块的名称。
python的模块既可以被调用，也可以独立运行。而被调用时``__name__``存储的是模块名(test1)，独立运行时存储的是``__main__``。它的作用主要就是用来区分，当前模块是独立运行还是被调用。

2. 如果test1是被作为模块调用的场合，把test2.py改为如下即可:
```python
def test():
	import test1
	print(test1.A)
```
test2在需要的时候才``import test1``,这时候可以确保test1已经初始化完成。
