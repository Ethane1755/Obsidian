---
title: Plt.pie 餅圖繪製
tags: #obsidian 
toc: true
season: winter
---
# Plt.pie 餅圖繪製
#python #Matplotlib 

```python
import matplotlib.pyplot as plt

labels = 'p','y','t','h','o','n' # 標籤
sizes = [10,20,30,10,20,10] # 百分比
explode = (0,0,0.1,0,0,0) # 突出

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

plt.axis = ('equal') # 控制為平面
plt.show()
```
![[pie_chart.png]]

#### 202108062155