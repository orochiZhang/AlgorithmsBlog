记录一下可能用到的功能对应SQL语句

## 批量修改字段中一部分内容
```sql
update 表 set 字段=replace(字段,'被替换的字符串','替换后的字符串');
```

## 批量修改字段数值
update 表名称 set 字段名称 = 字段名称 + 1 [ where语句]   
比如说数据库中有一张student表，要想把id为1的学生成绩（score）加1则    
```sql
update student set score=score+1 where id = 1
```
如果不加where子句，默认该表所有score字段都增加1。


## 表复制
1. Create 语法
```sql
# mysql 特有语法，new_table是新的表名，old_table是被复制的表名
Create table new_table (Select * from old_table);
```

2. INSERT INTO SELECT
```sql
Insert into Table2(field1,field2,...) select value1,value2,... from Table1
```
要求目标表Table2必须存在，由于目标表Table2已经存在，所以我们除了插入源表Table1的字段外，还可以插入常量。
```sql
Insert into Table2(a, c, d) select a,c,5 from Table1
```

3. SELECT INTO FROM语句 MySQL不支持这种语法

## MySQL设置double的精度
设置longitude的长度为16，小数点后保留8位
```sql
ALTER TABLE `data` CHANGE `longitude` `longitude` DOUBLE(16,8) NOT NULL
```

## 分组统计
```sql
SELECT SUM(price),DATE_FORMAT(created_at,'%Y-%m-%d')as day,user_id FROM `items` GROUP BY `day`,`user_id`
```

## linux备份mysql数据库
进入到MySQL库目录，根据自己的MySQL的安装情况调整目录
```
cd /var/lib/mysql
```   
执行
```
mysqldump -u root -p databaseName>backup.sql  
```
输入密码即可。   
databaseName是数据库名字，backup.sql是备份出来的文件名。
