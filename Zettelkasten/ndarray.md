# ndarray
#python #NumPy

- ndarray為一多維數組對象，由兩部分構成
	- 實際數據
	- 描述實際數據的元數據
- ndarray一般要求所有元素數據類型相同，數據下標由0開始
- ndarray對象之屬性
	- .ndim: 秩，即軸的數量/維度之數量
	- .shape: 對象之尺度，對於矩陣，n行m列
	- .size: 對象元素的個數，相當於.shape中$n\times m$的值
	- .dtype: 對象的元素類型
	- .itemsize: 每個元素的大小，以字節為單位
- ndarray 元素類型: 
	- bool: 布林值(True/False)
	- intc: 與C語言中之int類型一致，一般為int32或int64
	- intp: 用於索引的常數，與C語言中之ssize_t一致，為int32或int64
	- int8: 字節長度的整數，取值[-128,127]
	- int16: 16位長度的整數，取值[-32768,32767]
	- int32: 32位長度的整數，取值[$-2^{31},2^{31} -1$]
	- int64: 64位長度的整數，取值[$-2^{63},2^{63} -1$]
	- uint8: 8位無符號整數，取值[0,255]
	- iint16: 16位無符號整數，取值[0,65535]
	- uint32: 32位無符號整數，取值[0,$2^{32}-1$]
	- uint64: 64位無符號整數，取值[0,$2^{64}-1$]
	- float16: 16位半精度浮點數: 1位符號位，5位指數，10位尾數
	- float32: 32位半精度浮點數: 1位符號位，8位指數，23位尾數
	- float64: 64位半精度浮點數: 1位符號位，11位指數，52位尾數
	- complex64: 複數類型，實部和虛部皆為32位浮點數
	- complex128: 複數類型，實部和虛部皆為64位浮點數
- EX. 計算$A^2+B^3$
	- A、B為一維數組
	- 傳統方式:
```python
def pySum():
	a = [0,1,2,3,4]
	b = [9,8,7,6,5]
	c = []
	
	for i in range (len(a)):
		c.append(a[i]**2 + b[i]**3)
		
		return c
print(pySum())
```
- NumPy 方式:
```python
import numpy as np

def npSum():
	a = np.array([[0,1,2,3,4]])
	b = np.array([[9,8,7,6,5]])
	
	c = a**2 = b**3
	
	return c
print(npSum())
```
- ndarray 實例
```python
a = np.array([[0,1,2,3,4],
			  [9,8,7,6,5]])
a.ndim
2

a.shape
(2.5)

a.size
10

a.dtype
dtype('int32')

a.itemsize
4
```
- ndarray數組建立
	- 從Python中之列表、元組等類型創立
```python
x=np.array(list/tuple)
x=np.array(list/tuple, dtype=np.float32)
```
- 使用NumPy中函數創立ndarray數組，如arrange、ones、zeros等
	- np.arange(n): 類似range函數，元素從0到n-1
	- np.ones(shape): 根據shape建立一個全1數組
	- np.zeros(shape): 根據shape建立一個全0數組
	- np.full(shape,val): 根據shape建立一個數組，每個元素值都是val
	- np.eye(n): 建立一個$n\times n$的矩陣，對角線為1，其他為0
- 從字節流(raw bytes)創立ndarray數組
- 從文件中讀取特定格式資料創立

#### 202108052140