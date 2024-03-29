## 最左匹配原则
组合索引: 包含两个或多个属性列的索引称为复合索引。   
假如有索引(name, age, gender)
如果查询的where子句按这样的顺序使用了这些字段，查询会使用索引。   
```
(name, age, gender)   
(name, age, )   
(name, )   
```
这样的顺序则不会使用索引。   
```
(age, gender)   
(name, gender)    
(gender, )   
(age, )   
```
这就是最左匹配原则。


## 索引类型
索引类型分为:
1. clustered index 聚簇索引，主键索引，一级索引，聚集索引
2. secondary index 非聚簇索引，非主键索引，二级索引

聚簇索引的叶子节点存的是整行数据。
非聚簇索引的叶子节点内容是主键的值。

聚簇索引

聚簇索引默认是主键索引，如果表中没有定义主键，InnoDB 会选择一个唯一的非空索引代替。如果没有这样的索引，InnoDB 会隐式定义一个主键来作为聚簇索引。
因为B+TREE的原因，最好使用连续的整数字段，更好确定查找访问范围

## 回表

聚簇索引的叶子节点包含整行数据，所以只需要一次查询。
非聚簇索引的查询的结果只有主键ID，然后根据主键ID再查询一次数据库，得到结果，这就是回表。

1. select Name from TEST where ID=500，按主键查询，只需要搜索聚簇索引即可得到完整的数据，查询一次即可得到结果。
2. select Name from TEST where age=20，普通索引查询方式。
    1. 需要先搜索 age 二级索引，得到 ID 的值为 100
    2. 再到聚簇索引搜索一次。一共两次。

## 覆盖索引
1. 假设有非聚簇索引index(age)，查询select ID from TEST where age=20，通过 age 二级索引可以得到ID，满足查询结果需求，不需要进行回表查询。
索引 age 已经“覆盖了”查询需求，称为覆盖索引(Covering Index)。
2. 覆盖索引对于InnoDB引擎的MySQL表尤其有用，因为InnoDB使用聚集索引组织数据，如果二级索引中包含查询所需的数据，就不再需要在聚集索引中查找了。
3. 查询的时候使用INNODB 的聚簇索引也是覆盖索引。
4. 覆盖索引也并不适用于任意的索引类型，索引必须存储列的值。
5. Hash 和full-text索引不存储值，因此MySQL只能使用B-TREE。
6. 不同的存储引擎实现覆盖索引都是不同的。
7. 并不是所有的存储引擎都支持覆盖索引。

## 索引下推
1. 索引下推主要是为了减少二级索引的回表次数
2. 索引下推是MySQL5.6版本推出的优化手段，默认是开启的，可以通过下面命令关闭
    ```
    SET optimizer_switch = 'index_condition_pushdown=off';
    ```
3. 假如有index(name,age)，执行如下的sql：
    ```
    select * from user where name like '张%' and age=20 ;
    ```
4. 如果没有索引下推：
    1. MySQL会通过索引(name, age)获取到所有name = '张%'的ID，然后去一级索引查询（回表）完整的数据。
    2. 然后把结果进行筛选，获得age=20的数据。
5. 如果有索引下推：
    1. MySQL会通过索引(name, age)获取到所有name = '张%'的ID。
    2. 然后把1的结果进行age匹配，获得age=20的ID，得到结果2。
    3. 最后根据2的结果的ID，去一级索引查询（回表）完整的数据。
    4. 减少不必要的回表数据查询。


## 紧凑索引与松散索引
为什么你用了max函数就会用到松散扫描呢？请看使用松散索引扫描的条件。
当mysql 在group by 时 发现不能满足紧凑扫描时，尝试松散扫描(这相对于紧凑效率会率高，具体我尚未测试过)，如果连松散都不能用，那么可能会用到临时表或者文件排序。

要利用到松散索引扫描实现GROUP BY，需要至少满足以下几个条件：
1. GROUP BY 条件字段必须在同一个索引中最前面的连续位置；
2. 在使用GROUP BY 的同时，只能使用MAX 和MIN 这两个聚合函数；
3. 如果引用到了该索引中GROUP BY 条件之外的字段条件的时候，必须以常量形式存在；

## 使用索引进行排序

MySQL中，有两种方式生成有序结果集：一是使用filesort，二是按索引顺序扫描

利用索引进行排序操作是非常快的，而且可以利用同一索引同时进 行查找和排序操作。当索引的顺序与ORDER BY中的列顺序相同且所有的列是同一方向(全部升序或者全部降序)时，可以使用索引来排序，如果查询是连接多个表，仅当ORDER BY中的所有列都是第一个表的列时才会使用索引，其它情况都会使用filesort

## 不能使用索引的排序
当MySQL不能使用索引进行排序时，就会利用自己的排序算法(快速排序算法)在内存(sort buffer)中对数据进行排序，如果内存装载不下，它会将磁盘上的数据进行分块，再对各个数据块进行排序，然后将各个块合并成有序的结果集（实际上就是外排序）

对于filesort，MySQL有两种排序算法

1、两遍扫描算法(Two passes)

实现方式是先将须要排序的字段和可以直接定位到相关行数据的指针信息取出，然后在设定的内存（通过参数sort_buffer_size设定）中进行排序，完成排序之后再次通过行指针信息取出所需的Columns
注：该算法是4.1之前采用的算法，它需要两次访问数据，尤其是第二次读取操作会导致大量的随机I/O操作。另一方面，内存开销较小


2、 一次扫描算法(single pass)

该算法一次性将所需的Columns全部取出，在内存中排序后直接将结果输出
注： 从 MySQL 4.1 版本开始使用该算法。它减少了I/O的次数，效率较高，但是内存开销也较大。如果我们将并不需要的Columns也取出来，就会极大地浪费排序过程所需要 的内存。在 MySQL 4.1 之后的版本中，可以通过设置 max_length_for_sort_data 参数来控制 MySQL 选择第一种排序算法还是第二种。当取出的所有大字段总大小大于 max_length_for_sort_data 的设置时，MySQL 就会选择使用第一种排序算法，反之，则会选择第二种。为了尽可能地提高排序性能，我们自然更希望使用第二种排序算法，所以在 Query 中仅仅取出需要的 Columns 是非常有必要的。

当对连接操作进行排序时，如果ORDER BY仅仅引用第一个表的列，MySQL对该表进行filesort操作，然后进行连接处理，此时，EXPLAIN输出“Using filesort”；否则，MySQL必须将查询的结果集生成一个临时表，在连接完成之后进行filesort操作，此时，EXPLAIN输出 “Using temporary;Using filesort”


## MySQL找出从未使用过的索引

除了冗余索引和重复索引，可能还会有一些服务器永远不使用的索引，这样的索引完全是累赘，建议考虑删除，有两个工具可以帮助定位未使用的索引：

1.在percona server或者mariadb中先打开userstat=ON服务器变量，默认是关闭的，然后让服务器运行一段时间，再通过查询`information_schema.index_statistics`就能查到每个索引的使用频率。

2.使用percona toolkit中的pt-index-usage工具，该工具可以读取查询日志，并对日志中的每个查询进行explain操作，然后打印出关于索引和查询的报告，这个工具不仅可以找出哪些索引是未使用的，还可以了解查询的执行计划，如：在某些情况下有些类似的查询的执行方式不一样，这可以帮助定位到那些偶尔服务器质量差的查询，该工具也可以将结果写入到mysql的表中，方便查询结果。

## 常见问题
1. 为什么用 B+ 树做索引而不用哈希表做索引?   
哈希表不支持范围搜索。

## 索引注意事项
- 不要在列上使用函数，这将导致索引失效而进行全表扫描。
- 尽量避免使用 != 或 not in或 <> 等否定操作符。
- 多个单列索引并不是最佳选择，最好遵循复合索引的最左前缀原则。
- 索引不会包含有NULL值的列。
- 避免隐式转换的影响索引失效，比如 date_str 是字符串，然而匹配的是整数类型。
- 避免 like 语句的索引失效问题，“张%"是可以走索引，”%张“是不能走索引。
- 索引不要建在text这类很长的字符串类型。
- 对于查询中很少涉及的列或者重复值比较多的列，不宜建立索引。
- 在最频繁使用的、用以缩小查询范围的字段，需要排序的字段上建立索引。

## SQL优化
- 建索引，在频繁查询的几个字段上建立联合索引，通过索引覆盖，避免回表的问题，达到高效查询的效果。
- 减少表之间的关联
- 优化 sql，尽量让 sql 很快定位数据，不要让 sql 做全表查询，应该走索引, SQL where子句符合最左匹配原则。
- 尽量返回少量数据，没用的字段不要读取，不要使用select *。
- 尽量用PreparedStatement 来查询，不要用 Statement。

### 优化顺序
- 优化SQL, 加索引。
- 表数据过大，分库分表。
- 加硬件配置，换SSD。

## 参考文献
- [mysql5.7官方文档 group-by-optimization](https://dev.mysql.com/doc/refman/5.7/en/group-by-optimization.html)
- [mysql高效索引之覆盖索引](https://www.cnblogs.com/chenpingzhao/p/4776981.html)
- [mysql 松散索引与紧凑索引扫描](https://www.cnblogs.com/novice-dxx/p/11955920.html)
- [【mysql】索引 回表 覆盖索引 索引下推](https://www.cnblogs.com/lisq/p/12634457.html)

