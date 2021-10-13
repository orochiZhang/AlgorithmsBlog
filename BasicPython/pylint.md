# Python Pylint使用心得

## 屏蔽某一类型消息
```
disable="W"
```
表示屏蔽所有warning类型的消息。   
```
disable="E1101"
```
表示屏蔽1101的错误信息。

## 屏蔽某些动态属性的报错
1. 在python类里面有一些属性是动态生成。为了防止这些内容被当成报错。
ignored-classes=optparse.Values,thread._local,_thread._local

2. 在实际开发的时候，我遇到过在python底层新增的函数。比如新增一个字符串操作的函数a1。这个在pylint会报错没有这个函数。
    1. 用ignored-classes=str.a1是没法屏蔽这个报错。
    2. 直接用ignored-classes=a1来屏蔽这种报错


## 屏蔽builtins的报错
在实际开发的时候，我遇到过在python底层新增一个函数，或者一个变量。比如新增变量a。这个在pylint会报错没有这个变量。但是实际运行没问题。  
这时候需要使用``additional-builtins``来屏蔽这个问题。
```
additional-builtins=a
```
   

## 屏蔽不存在的import的报错
如果你检查的项目只是一个大项目的其中一个部分，项目可能import了一些外部项目的类，但是pylint是找不到的。可以使用ignored-modules来忽略：
```
ignored-modules = a,b,c
```

## 使用注释忽略某一个告警
比如 line:13 func is not callable(E1102/not-callable)
可以使用
```
# pylint:disable=not-callable
```
或者
```
# pylint:disable=E1102
```
屏蔽多个错误的注释
```
# pylint:disable=E1102,E1103
```

## 注释的作用域
注释是有作用域的，同一个函数需要有个多次相同的告警忽略，建议在函数开头用注释声明。   
以免出现意外情况，比如如下情况：
```python
if xxx:
    for in:
        # pylint:disable=E1102 只忽略if里面的告警
else:
    # pylint:disable=E1102  这个注释无效
