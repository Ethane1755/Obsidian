---
title: Numpy 入門
tags: #obsidian 
toc: true
season: winter
---
# Numpy 入門
#python #NumPy 
- 數組對象可以去掉"循環"之步驟，使一維向量更像一個數據
- 設定專門的數組對象，可以提升運算效率
- 節省儲存空間
引用NumPy: import numpy as np
```python
import numpy as np
```
輸入二維以下文件: n=np.loadtxt('檔案名稱',dtype,delimiter)
```python
a = np.loadtext('hello.csv',delimiter=",")
```
儲存二維以下文件: np.savetxt('文件名稱',存入文件的數組,格式,delimiter)
```python
np.savetxt('hello.csv',a,%d,delimiter=",")
```
將數組輸出至任意維度文件: a.tofile('文件名稱',數據分割字符串,數據格式)
```python
a.tofile('hello.bat',sep=",",format='%d')
```
輸入任意維度文件: np.fromfile('文件名稱',dtype, 讀入元素個數(-1為全文件),數據分割字符串)
```python
np.fromfile('hello.bat',dtype=np.int,sep=",")
```

將數組整理成不同形狀: .reshape(m,n)
```python
a=np.arange(100).reshape(5, 20)
```
#### 202108052151