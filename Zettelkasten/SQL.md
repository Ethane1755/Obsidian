# SQL
#SQL 


-  COLLATE 編碼
	- 中文 utf8mb4_unicode_ci



-  GROUP BY 資料分群
-  GRANT 授權使用者權限
	- GRANT 想要給其他使用者之權限 TO
-  REVOKE 取消使用者權限


- HAVING 函數條件
```SQL
SELECT 欄位1, 函數(欄位2)
FROM 表格
HAVING 函數條件
```

-  START TRANSACTION 開始包裝以下程式
-  COMMIT 提交
	- 一定要完成提交才會修改成功
-  ROLLBACK 取消操作(操作不對原始資料造成影響)

- 函數
	- COUNT 數量
	- SUM 加總
	- AVG 平均值
	- MAX 最大值
	- MIN 最小值
```SQL
SELECT 函數 (欄位)
FROM 表格;
```
-  VARCHAR 可變長度字串
-  INTEGER 整數
-  NOT NULL 此欄不能為空
-  每句以分號作結束
	- ;
-  星號代表所有
	- \*

