# SQL Test
#SQL
```SQL
CREATE DATABASE test 								--建立叫test的資料庫
COLLATE utf8mb4_unicode_ci;							--編碼
CREATE TABLE test (									--建立資料庫內容
	username VARCHAR(12) NOT NULL,
	age INTEGER,
	gender VARCHAR(6)
);
ALTER TABLE test ADD education TEXT;
INSERT INTO test VALUES(
	'Ethane', 15, 'Male', 'High School'
);

BEGIN TRANSACTION;

	SELECT age 										--選擇欄位
	FROM test 										--欄位在哪個資料庫
	WHERE age > 10 AND gender is 'Female'; 			--篩選

	SELECT * FROM test
	ORDER BY age DESC;								--依照age欄位由大到小排序

	SELECT COUNT(*)									--計算除了無資料以外的所有欄位
	FROM test;

	SELECT gender, COUNT(*)
	FROM test;
	GROUP BY gender;
	
	DELETE FROM test
	WHERE username = 'Ethane';
	
COMMIT;

SELECT username
FROM test

ROLLBACK;

```

#### 202108092148

