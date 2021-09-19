示例代码
```python
class A(object):

    def __init__(self):
        object.__init__(self)
    def hello(self):
        print ("A")

class B(object):

    def __init__(self):
        object.__init__(self)
    def hello(self):
        print ("B")

class C(B,A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        
class D(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

test = C()
test.hello() #B

test2 = D()
test.hello() #A
```

## MRO
```
  O
 /|\
D E F
\/\/
B  C
 \/
 A
```
在上面的类图中,可以通过极左原理来推算MRO的顺序,具体怎么做呢?
```
1.首先,从根开始,寻找没有被指向的,那么第一个就是A

2.如果有多个,根据极左原理选择最左的类,之后将这个类加入MRO,并且删除这个类以及和它相关的指向边,由此可以得出B和D

3.左边的指向边完了,再次根据极左原理寻找有指向边的父类,可以得出C和E

4.以此类推,只剩下了孤单的F了,当所有指向边都移除之后,就剩下了最后一个基类O

那么,我们最后就可以得到最终MRO的顺序为[A,B,D,C,E,F,O]
```
