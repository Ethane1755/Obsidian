---
title: SQL  資料定義(DDL)
tags: #obsidian 
toc: true
season: winter
---
# SQL  資料定義(DDL)
#SQL 

- CREATE DATABASE 建立資料庫
- CREATE TABLE 建立資料表
- ALTER TABLE 更改資料庫
	- 增加欄位
	- 刪除欄位
	- 更改資料類別
- DROP TABLE 刪除資料表 (完全刪除)
- TRUNCATE TABLE 刪除資料表內容，保留結構 (資料表還在，但資料已刪除)
- Constraint [[SQL]] 限制
	- NOT NULL 非空值限制
	- UNIQUE 唯一限制(該欄不能有重複資料)
	- PRIMARY KEY 主鍵限制 (類似UNIQUE+NOT NULL)
		- 當主鍵包含多欄位時，稱其為組合鍵
	- FOREIGN KEY 外鍵限制(將A資料表的某欄位對應到B資料表的主鍵欄位)
	- CHECK 檢查限制 (限制該欄資料條件)
	- DEFAULT 預設值限制 (若該欄位沒有輸入資料時自動填入甚麼)
- AUTO INCREMENT 自動編號
	- 不需要指定開始編號(預設為0)
	- 若需指定，直接在後面加上 *=數字 *
- INDEX 索引
- VIEW 檢視(能操作不能修改)


```SQL
#CREATE
CREATE DATABASE test
CREATE TABLE test2(
	column1 PRIMARY KEY
);
CREATE TABLE test_1(
	column_name1 datatype NOT NULL,
	column_name2 datatype UNIQUE,
	column_name3 datatype PRIMARY KEY,
	column_name4 datatype CHECK (column_name1 > 0),
	column_name5 datatype DEFAULT '未知',
	column_name6 datatype AUTOINCREMENT = 2
	FOREIGN KEY [column_name1] REFERENCES test2 [column1]
);

#ALTER
ALTER TABLE test_1 ADD column_1 datatype;
ALTER TABLE test_1 ADD CHECK (column_name2 < 1);
ALTER TABLE test_1 ALTER COLUMN column_name1 SET DEFAULT '未知';
ALTER TABLE DROP COLUMN column_2;
ALTER TABLE test_1 ALTER COLUMN column_name1 datatype;

#DROP/TRUNCATE
DROP TABLE test_1;
TRUNCATE TABLE test_1;
DROP DATABASE test;

#INDEX
CREATE INDEX '索引1' ON test_1(column_name1, column_name2);

#VIEW
CREATE VIEW view_1(column_name1, column_name2) AS
SELECT column_name1, column_name2 * column_name3 FROM test_1
GROUP BY column_name1;
```

#### 202108161659