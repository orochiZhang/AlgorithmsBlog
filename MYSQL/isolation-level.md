## sql隔离等级
关于隔离级别的理解

1.read uncommitted    
读取未提交的数据（脏读），举个例子：别人说的话你都相信了，但是可能他只是说说，并不实际做。

2.read committed    
读取已提交的数据。但是，可能多次读取的数据结果不一致（不可重复读，幻读）。用读写的观点就是：读取的行数据，可以写。

3.repeatable read(MySQL默认隔离级别)    
可以重复读取，但有幻读。读写观点：读取的数据行不可写，但是可以往表中新增数据。在MySQL中，其他事务新增的数据，看不到，不会产生幻读。采用多版本并发控制（MVCC）机制解决幻读问题。

4.serializable    
可读，不可写。像java中的锁，写数据必须等待另一个事务结束。

- 数据库默认隔离级别:  
    - mysql : read repeatable (RR)
    - oracle,sql server: read commited (RC)
- mysql binlog的格式三种：statement, row, mixed
- 为什么mysql用的是repeatable而不是read committed:在 5.0之前只有statement一种格式，而主从复制存在了大量的不一致，故选用 read repeatable
- 为什么默认的隔离级别都会选用 read commited
    - read repeatable存在间隙锁会使死锁的概率增大，在 read repeatable (RR) 隔离级别下，条件列未命中索引会锁表.
    - 而在 read commited (RC) 隔离级别下，只锁行.
- 在RC级用别下，主从复制用什么binlog格式：row格式，是基于行的复制！
- 使用 read commited (RC) 的原因
    - 原因1：在 read repeatable (RR) 隔离级别下，存在间隙锁，导致出现死锁的几率比 read commited (RC) 大的多。
    - 原因2：在 read repeatable (RR) 隔离级别下，条件列未命中索引会锁表！而在 read commited (RC) 隔离级别下，只锁行。
    - 原因3：在 read commited (RC) 隔离级别下，半一致性读(semi-consistent)特性增加了update操作的并发性。
- **半一致性读(semi-consistent)** ，如果update的记录发生锁等待，那么返回该记录的prev 版本（在返回前会将锁等待的这个lock从trx中删除掉），到mysql层进行where判断，是否满足条件。如果满足where条件，那么再次进入innodb层，真正加锁或者发生锁等待。
- 间隙锁（Gap Lock），目的是防止幻读
    - 防止间隙内有新数据被插入
    - 防止已存在的数据，更新成间隙内的数据(例如防止numer=3的记录通过update变成number=5)
    - innodb自动使用间隙锁的条件：
        1. 必须在RR级别下
        2. 检索条件必须有索引，没有索引的话，mysql会全表扫描，那样会锁定整张表所有的记录，包括不存在的记录，此时其他事务不能修改不能删除不能添加。
- RR级别下，事务中的第一个SELECT请求才开始创建read view；
- RC级别下，事务中每次SELECT请求都会重新创建read view； 

- for update的使用场景
    - 如果遇到存在高并发并且对于数据的准确性很有要求的场景，是需要了解和使用for update的。
    - 比如涉及到金钱、库存等。一般这些操作都是很长一串并且是开启事务的。如果库存刚开始读的时候是1，而立马另一个进程进行了update将库存更新为0了，而事务还没有结束，会将错的数据一直执行下去，就会有问题。所以需要for update 进行数据加锁防止高并发时候数据出错。
    - 记住一个原则：一锁二判三更新

### 范围
next-key-lock
-  加锁的单位是next-key-lock；
-  只有访问到的对象才会加锁；
-  对于唯一索引的等值查询来说，next-key-lock会退化为行锁；
-  索引的等值查询来说，向右遍历时，右边界不满足等值条件时，next-key-lock会退化为间隙锁；
-  对于唯一索引的范围查询来说，会访问到第一个不满足条件的记录为止。

举例1
```
id	name	age
1	JAMES	37
2	OVEN	28
3	LOVE	34
```
如果age是索引的话，相关的区域有
```
(-无穷,28]
(28,34]
(34,37]
(37,+无穷)
```
如果执行如下语句：
```
select * from  people where age =34 for update;
```
那么会锁住(28,37)这么范围


举例2
唯一索引  2，4，8，16， 32，查找 id>=8 and id<9

1. 要找的第一行是 id = 8，因此 next-key lock(4,8]，但是由于 id 是唯一索引，且该记录是存在的，因此会退化成记录锁，也就是只会对 id = 8 这一行加锁；
2. 范围查找，就会继续往后找存在的记录，也就是会找到 id = 16 这一行停下来，然后加 next-key lock (8, 16]，但由于 id = 16 不满足 id < 9，所以会退化成间隙锁，加锁范围变为 (8, 16)。

## 参考文献

- [mysql的默认隔离级别](https://www.cnblogs.com/shoshana-kong/p/10516404.html)

- [mysql中binlog_format的三种模式](https://www.cnblogs.com/xingyunfashi/p/8431780.html)

- [MySQL的四种事务隔离级别](https://www.cnblogs.com/huanongying/p/7021555.html)

- [MVCC实现机制](https://www.cnblogs.com/luchangyou/p/11321607.html)

- [mysql记录锁、间隙锁、临键锁](https://blog.csdn.net/weixin_39406430/article/details/125464315)
