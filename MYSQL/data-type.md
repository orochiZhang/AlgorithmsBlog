## int类型

name | size(字节)
---|---
bigint | 8
int| 4
medium int | 3
small int | 2
tinyint | 1


1. int(M) 在 integer 数据类型中，M 表示最大显示长度。
2. 在 int(M) 中，M 的值跟 int(M) 所占多少存储空间并无任何关系。 int(3), int(4), int(8)在磁盘上都是占用 4 btyes 的存储空间。
3. 如果int的值为10, int（10）显示结果为0000000010, int（3）显示结果为010。


## varchar/nvarchar 和 char/nchar区别
- varchar/nvarchar的实际存储空间是可变长的，char/nchar的存储空间是定长的。
- nchar，nvarchar是以Unicode字符存储，即所有字符都占两个字节。
- 支持多语言的站点应考虑使用 nchar 或 nvarchar，以尽量减少字符转换问题。 

### varchar 和 char
- varchar(100) 与 varchar(200)存储90个字节的字符串真的相同吗? 结果是否定的。    
    1. 硬盘上的存储空间虽然都是根据实际字符长度来分配存储空间的。varchar(100) 与 varchar(200)的存储空间相同。     
    2. 对于内存来说，则使用字符类型中定义的长度的内存块来保存值。即 varchar(200)使用200个字符空间，varchar(100)使用100个字符空间。
- char(1) 与 varchar(1)两这个定义，会有什么区别呢?  
虽然这两个都只能够用来保存单个的字符，但是 varchar 要比 char 多占用一个存储位置。这主要是因为使用VARCHAR数据类型时，会多用1个字节用来存储长度信息。这个管理上的开销 char 字符类型是没有的。

### varchar最大长度
mysql的vachar字段的类型虽然最大长度是65535，但是并不是能存这么多数据。具体按以下情况讨论：
1. 不允许非空字段的时候，最大可以到65533。
2. 当允许非空字段的时候只能到65532。在允许空的时候，varchar(65535) = 2 bytes (length) + 65532 chars (latin1) + 1 byte (is null) 

### 使用char的好处
1. 从碎片角度进行考虑，使用CHAR字符型时，由于存储空间都是一次性分配的，不存在碎片的困扰。
2. 可变长度的字符数据类型，其存储的长度是可变的。当其更改前后数据长度不一致时，就不可避免的会出现碎片的问题。
3. 如果一个VARCHAR经常被修改，而且每次被修改的数据的长度不同，这会引起‘行迁移’(Row Migration)现象，而这造成额外的I/O消耗。
4. 如果某个字段其长度虽然比较长，但是其长度总是近似的，如一般在90个到100个字符之间。或者是相同的长度。这种情况比较适合使用CHAR字符类型。如MD5哈希值，身份证号码，手机号码等等。

### 关于索引
如果在一个char或者varchar列上建立唯一索引之后，那么'a'和'a '，会引起duplicate-key error。

## 时间类型
常用的记录时间的类型有
1. int 直接记录时间戳
2. timestamp
3. datetime



## 参考文献
- [varchar/nvarchar 和 char/nchar区别](https://blog.csdn.net/huangli1466384630/article/details/79831688)
- [Mysql 数据库字符类型详解](https://www.cnblogs.com/xuchunlin/p/6235369.html)
