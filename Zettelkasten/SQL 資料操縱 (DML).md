---
title: SQL 資料操縱 (DML)
tags: #obsidian 
toc: true
season: winter
---
# SQL 資料操縱 (DML)
#SQL 
- INSERT INTO 新增資料
- UPDATE  更新資料
- DELETE FROM  刪除資料
- SELECT INTO 將A資料表查詢得到的資料新增至B資料表中
```SQL
#INSERT INTO
INSERT INTO test_1 (column_name1,column_name2)
VALUES (value1,value2);
	#另一種寫法
INSERT INTO test_1
VALUES(value1,value2);	#若採用此寫法，每欄的資料都必須寫出來
#UPDATE
UPDATE test_1
SET column_name1 = value1, column_name2 = value2
WHERE column_name3 = value3;
#DELETE FROM
DELETE FROM test_1
WHERE column_name1 = value1;
#SELECT INTO
SELECT column_name1, column_name2
INTO test_2 [IN another_database]
FROM test_1;
```
#### 202108162037