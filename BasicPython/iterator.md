1. 列表，元组，字符串，迭代器，生成器都是可迭代对象。所以，可迭代对象不一定是迭代器，生成器。

2. 可迭代对象传递给iter()方法可以得到该对象的迭代器。
3. 迭代器也是可迭代对象的一种，所以将一个迭代器传递给iter()方法，总是会得到其本身。

4. for…in…实际上是对可迭代对象的迭代，实现逻辑如下：   
   1. 对可迭代对象使用iter()方法获得迭代器   
   2. 对迭代器使用next()反复从迭代器中获得下一项   
   3. 如果我们成功获得下一项，就执行 for 循环的逻辑   
   4. 如果我们在获得下一项时得到了一个 StopIteration 异常，那么就捕抓这个异常并停止循环

5. 生成器是一种只能迭代一次的迭代器。所以，迭代器不一定是生成器。
例如：
```python
# 生成器全部消耗的例子
numbers = [1, 2, 3, 5, 7]
squares = (n ** 2 for n in numbers)
print(list(squares))		//输出 [1, 4, 9, 25, 49]
print(list(squares))		//输出 [ ]

# 生成器局部消耗的例子
numbers = [1, 2, 3, 5, 7]
squares = (n ** 2 for n in numbers)
if 9 in squares:
    print('yes')
else:
    print('no')
if 9 in squares:
    print('yes')
else:
    print('no')
# 最后输出 yes, no
```
参考文献：   
- http://python.jobbole.com/89181/  
- https://www.cnblogs.com/leomei91/p/7356752.html   
