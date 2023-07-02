怎么设计这么一个 randomLevel() 方法呢？直接撸代码：
```
// 该 randomLevel 方法会随机生成 1~MAX_LEVEL 之间的数，且 ：
//        1/2 的概率返回 1
//        1/4 的概率返回 2
//        1/8 的概率返回 3 以此类推
private int randomLevel() {
  int level = 1;
  // 当 level < MAX_LEVEL，且随机数小于设定的晋升概率时，level   1
  while (Math.random() < SKIPLIST_P && level < MAX_LEVEL)
    level += 1;
  return level;
}
```


上述代码可以实现我们的功能，而且，我们的案例中晋升概率 SKIPLIST_P 设置的 1/2，即：每两个结点抽出一个结点作为上一级索引的结点。如果我们想节省空间利用率，可以适当的降低代码中的 SKIPLIST_P，从而减少索引元素个数，Redis 的 zset 中 SKIPLIST_P 设定的 0.25。

## Python实现的跳表
```python
# -*- coding: utf-8 -*-
import random

HEAD = 1
TAIL = 2
DATA = 3

TYPE_TUPLE = ('', 'HEAD', 'TAIL', 'DATA')

SKIPLIST_P = 1/2


class IndexError(Exception):  
    # 创建一个新的exception类来抛出自己的异常。
    # 异常应该继承自 Exception 类，包括直接继承，或者间接继承
    def __init__(self, errorinfor):
        self.error = errorinfor
    
    def __str__(self):
        return self.error

class Node(object):
    def __init__(self, type, key, value, level):
        self.key = key
        self.value = value
        self.type = type
        self.level = level
        self.next_list = [None] * level
        self.pre_list = [None] * level
    
    def __str__(self):
        return '<Node %s key: %s levle: %s>' % (TYPE_TUPLE[self.type], self.key, self.level)
    
    def set_next(self, level, node):
        if level >= len(self.next_list):
            raise IndexError('level error %s %s %s' % (self, self.level, level))
        else:
            self.next_list[level] = node
            
    def get_next(self, level):
        if level >= len(self.next_list):
            raise IndexError('level error %s %s %s' % (self, self.level, level))
        else:
            return self.next_list[level]

    def set_pre(self, level, node):
        if level >= len(self.next_list):
            raise IndexError('level error %s %s %s' % (self, self.level, level))
        else:
            self.pre_list[level] = node

    def get_pre(self, level):
        if level >= len(self.next_list):
            raise IndexError('level error %s %s %s' % (self, self.level, level))
        else:
            return self.pre_list[level]
        
    def update_value(self, value):
        self.value = value
    
    def get_key(self):
        if self.type == HEAD:
            return 'head'
        if self.type == TAIL:
            return 'tail'
        return self.key
    
    def remove(self):
        if self.type == DATA:
            for i in range(self.level):
                pre = self.pre_list[i]
                next = self.next_list[i]
                pre.set_next(i, next)
                next.set_pre(i, next)
            

class SkipList():
    
    def __init__(self, level):
        self.level = level - 1
        self.head_list = []
        head_node = Node(HEAD, None, None, level)
        tail_node = Node(TAIL, None, None, level)
        for i in range(level):
            head_node.set_next(i, tail_node)
            tail_node.set_pre(i, head_node)
        self.head = head_node
        self.tail = tail_node

    def random_level(self):
        level = 1
        #当 level < MAX_LEVEL，且随机数小于设定的晋升概率时，level + 1
        while (random.random() < SKIPLIST_P and level < self.level):
            level += 1
        return level
    
    def add_node(self, key, value):
        level = self.random_level()
        node = Node(DATA, key, value, level)
        self.add_node_in_level(level-1, node)
        
    def add_node_in_level(self, level, node):
        find_level = self.level
        pre_node = self.head
        next_node = self.tail
        while find_level >= 0:
            next_node = pre_node.get_next(find_level)
            if next_node is self.tail:
                if find_level <= level:
                    self.insert_node(pre_node, next_node, node, find_level)
                find_level -= 1
                
            elif next_node.get_key() > node.get_key():
                if find_level <= level:
                    self.insert_node(pre_node, next_node, node, find_level)
                find_level -= 1
            else:
                pre_node = next_node
    
    def insert_node(self, pre_node, next_node, node, level):
        pre_node.set_next(level, node)
        next_node.set_pre(level, node)
        node.set_next(level, next_node)
        node.set_pre(level, pre_node)
    
    def remove_node(self, key):
        node = self.get_node(key)
        if node:
            node.remove()
    
    def update_node(self, key, value):
        node = self.get_node(key)
        if node:
            node.update_value(value)
    
    def get_node(self, key):
        find_level = self.level
        pre_node = self.head
        while find_level >= 0:
            node = pre_node.get_next(find_level)
            if node is self.tail or node.get_key() > key:
                find_level -= 1
            elif node.get_key() == key:
                return node
            else:
                pre_node = node
        return None
    
    def travel(self):
        find_level = self.level
        pre_node = self.head
        key_list = []
        while find_level >= 0:
            node = pre_node.get_next(find_level)
            key_list.append(str(node.get_key()))
            if node is self.tail:
                print("->".join(key_list))
                key_list = []
                pre_node = self.head
                find_level -= 1
            else:
                pre_node = node


if __name__ == '__main__':
    
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    skiplist = SkipList(5)
    for number in number_list:
        skiplist.add_node(number, number)
    
    skiplist.travel()
    result = skiplist.get_node(4)
    print('>>>>', result)
    skiplist.remove_node(4)
    skiplist.travel()
    result = skiplist.get_node(4)
    print('>>>>',result)
```

