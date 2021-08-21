# SQL 資料查詢(DQL)
#SQL 
- SELECT
	- 想要尋找的欄位
	- 若要取得整張資料表-> **\*** 符號
		- 盡量避免(耗時)
- WHERE
	- 篩選器(增加條件)
	- 在其中使用AND
		- AND兩邊條件都要符合
	- 在其中使用OR
		- OR兩邊條件只要符合一邊即可
-  ORDER BY 排序
	- DESC 由大到小
	- ASC 由小到大
- SELECT DISTINCT
	-  想要尋找之欄位(同一內容只會顯示一次)
- TOP 選擇前幾筆資料
- IN 符合
	- 可配合NOT
- BETWEEN 在A與B之間(包含A、B)
- 萬用字元 Wildcards
	- _ 底線
		- 代表一個字元
		- 'A_Z'
			- 所有A開頭，Z結尾，共三個字元的資料
		- '_ AN%'
			- 代表所有第二個字為A，第三個字為N的資料
	- % 百分比
		- 代表零個/一個/多個字元
		- 'ABC%'
			- 代表所有ABC開頭的資料
		- '%XYZ%' 
			- 代表所有包含XYZ的資料 
	- [] 方括號 
		- 包含其中字元
		- a[bcd]
			- 包含ab, ac, ad 
	- [^]方括號中向上符號
		- 不包含其中字元
		- a\[^bcd\]
			- 包含除ab, ac, ad外a開頭的資料
- LIKE
- AS
- JOIN
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- CROSS JOIN
- NATURAL JOIN
- UNION
- INTERSECT
- MINUS
- 子查詢 Subquery
- EXISTS
- CASE
- Date
```SQL
#SELECT
SELECT 欄位 FROM 表格;
#WHERE
SELECT 欄位
FROM 表格
WHERE 條件1 AND 條件2 OR 條件3;
#ORDER BY
SELECT * FROM 表格
ORDER BY 欄位1 ASC, 欄位2 DESC;
#DISTINCT
SELECT DISTINCT 欄位 
FROM 表格;
#TOP
SELECT TOP (30) 欄位1, 欄位2
FROM 表格
	#OR
SELECT TOP (30) PERCENT 欄位3
FROM 表格
#IN
SELECT 欄位 FROM 表格
WHERE 欄位
IN (條件1, 條件2);
#BETWEEN
SELECT 欄位1, 欄位2
FROM 表格
WHERE 欄位1
BETWEEN 數值1 AND 數值2;
```

0928209222