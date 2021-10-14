collections 模块----Python标准库，是数据结构常用模块

常用类型有：

1. **Counter** 计数器 主要功能：将元素数量统计，然后计数返回一个字典，键为元素，值为元素个数

2. **deque** 双向队列，双向链表

3. **defaultdict** 默认字典，字典的一个子类，继承所有字典的方法，默认字典在进行定义初始化的时候得指定字典值有默认类型。    
重写了dict的__missing__(key)方法，当通过中括号方式【底层调用__getitem__方法获取值】获取defaultdict实例中不存在的键的值时__getitem__方法会进一步调用__missing__方法，然后__missing__会调用default_factory，如果None时raise KeyError，如果可调用对象时调用该对象，返回值作为键的值添加到defaultdict中，且返回value值

4. **OrderedDict** 有序字典也是字典的一个子类，使用双向链表维护顺序有序。
5. **namedtuple** namedtuple由自己的类工厂namedtuple()进行创建，而不是由表中的元组进行初始化，通过namedtuple创建类的参数包括类名称和一个包含元素名称的字符串

