---
title: SQL 運算子
tags: #obsidian 
toc: true
season: winter
---
# SQL 運算子
#SQL

- 算術運算子 Arithmetic Operators
	- \+
		- 加法
	- \-
		- 減法
	- \*
		- 乘法
	- /
		- 商(除法)
	- %
		- 餘數(除法)
- 邏輯運算子 Logical Operators
	- AND 多重條件
	-  OR 或(條件)
	-  NOT 非(條件)
- 比較運算子 Comparison Operators
	- \> 
		- 大於
	- \<
		- 小於
	- \<=
		- 小於等於
	- \>=
		- 大於等於
	- =
		- 等於
	- <>  
		- 不等於
	-  IN 選擇多個資料值
	- BETWEEN 在...之間
	- LIKE 符合

```SQL
SELECT *
FROM 表格
WHERE 欄位 LIKE '模式';

SELECT *
FROM 表格
WHERE 欄位 IN (條件1,條件2);

SELECT 欄位
FROM 表格
WHERE 條件
OR(條件1 AND 條件2);

SELECT *
FROM 表格
WHERE 欄位 BETWEEN '條件1' AND '條件2';
```

#### 202108161607