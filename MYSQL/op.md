# MySQL 操作笔记

## drop、delete与truncate的区别


- Delete 用来删除表的全部或者一部分数据行。
	- 执行delete之后，用户需要提交(commmit)或者回滚(rollback)来执行删除或者撤销删除。
	- Delete会触发这个表上所有的delete触发器
- Truncate 删除表中的所有数据。
	- Truncate 这个操作不能回滚，也不会触发这个表上的触发器。
	- Truncate 执行比 Delete 更快。
- Drop 是从数据库中删除表。
	- 表的所有的数据行，索引和权限也会被删除。
	- 所有的DML触发器也不会被触发。
	- Drop 这个命令也不能回滚。


