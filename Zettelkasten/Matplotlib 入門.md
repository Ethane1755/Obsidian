# Matplotlib 入門
#python #Matplotlib
- 引用Matplotlib: import matplotlib.pyplot as plt
- 輸入資料: plt.plot([第一組資料],[第二組資料])
- 可使用LaTeX
- 各類圖表
- 
| 函數 | 說明 | 
| ---- | ---- |
| plt.plot | 折線圖 | 
| plt.boxplot | 箱型圖 | 
| plt.bar | 柱狀圖|
| plt.barh | 橫向柱狀圖|
| plt.polor | 雷達圖 |
| plt.pie | 圓餅圖 |
| plt.psd | 功率譜密度圖 |
| plt.specgram | 譜圖 |
| plt.cohere | X-Y關係的函數圖 |
| plt.scatter | 散點圖 |
| plt.step | 步階圖 |
| plt.hist | 直方圖 |

- 軸標籤: plt.軸名稱label
- 標題: plt.title()
- 任意地方增加文字:  plt.text()
- 帶箭頭之註解: plt.annotate()
	- plt.annotate('文字',指向點xy座標=,文字座標=,arrowprops=dict(facecolor顏色,shrink箭頭端點與圖形距離,width箭頭寬度))
- 軸尺度: plt.axis([橫軸起始點,橫軸終止點,縱軸起始點,縱軸終止點])
- 網格: plt.grid(True/False)
- 顯示圖表: plt.show()
- 將圖表儲存成png: plt. savefig('路徑/名稱',dpi=)
- 創立多個繪圖區域: plt.subplot(分割橫軸條數,分割縱軸條數,定位至哪一個區域)
- 中文字: plt.軸labels('軸名稱', fontproperties='字體', fontsize=)
- 多條曲線: plt.plot(x軸,y軸,x1軸,y1軸...)
- x,y軸限制: plt.x/y lim
- 圖例: plt.legends()
	- 要先創立label欄
- 曲線格式:plt.plot(x軸,y軸,**format_string**)
- format_string
	- 顏色
		- 'b' : 藍
		- 'g' : 綠
		- 'r' : 紅
		- 'c' : 青
		- 'm' : 洋紅
		- 'y' : 黃
		- 'k' : 黑
		- 'w' : 白
		- '#000000' : HEX色碼
		- '0.8' : 灰度值
	- 風格
		- '-' : 實線
		- '--' : 破折線
		- '-.' : 點劃線
		- ':' : 虛線
		- ' ' :無線條
	- 標記
		- '.' : 點標記
		- ',' : 像素點(極小)
		- 'o' : 實心圈
		- 'v' : 倒三角
		- '^' : 上三角
		- '>' : 右三角
		- '<' : 左三角
		- '1' : 下花三角
		- '2' : 上花三角
		- '3' : 左花三角
		- '4' : 右花三角
		- 's' : 實心方形
		- 'p' : 實心五角形
		- '\*' : 星形
		- 'h' : 直六角形
		- 'H' : 橫六角形
		- '+' : 十字
		- 'x' : X
		- 'D' : 菱形
		- 'd' : 細菱形
		- '|' : 垂直線
- EX. 
```python
import matplotlib.pyplot as plt
plt.plot([3,1,2,4,5])
plt.ylabel("grade")
plt.savefig('D:/Database/Python/.spyder-py3/first', dpi=600)
plt.show()
```
- Workflow
	- 準備資料
	- 建立圖表
	- 客製化圖表
	- 儲存圖表
	- 展示圖表




#### 202108062155-1