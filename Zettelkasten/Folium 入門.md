---
title: Folium 入門
tags: #obsidian 
toc: true
season: winter
---
# Folium 入門
#python #Folium

**folium.Map()**
其中參數:
- location=[a,b] :  中心點經緯度(先緯後經)
- width=$\sum$%: 寬度
- height=$\sum$%: 高度
- tiles=$\alpha$:地圖樣式
	- “OpenStreetMap”![[Pasted image 20210811181457.png]]
	- “Stamen” (Terrain,![[Pasted image 20210811181614.png]] Toner,![[Pasted image 20210811181634.png]] and Watercolor)![[Pasted image 20210811181654.png]]
	- “CartoDB” (positron![[Pasted image 20210811181339.png]] and dark_matter)![[Pasted image 20210811181409.png]]
- min_zoom=$\sum$: 最大放大多少
- max_zoom=$\sum$: 最小放大多少
- start_zoom=$\sum$: 原始縮放率
- control_scale=$\beta$: 固定比例尺
- disable_3d=$\beta$: 3D支持
- zoom_control=$\beta$: 縮放按鍵
- no_touch=$\beta$: 不互動
- prefer_canvas=$\beta$: 渲染器，在資訊量大時若設為$True$可提升效能

**map.add_child(folium.Marker())**
其中參數:
- location = [a,b] :經緯度
- popup = '$\alpha$': 點擊後彈出文字
- icon = folium.Icon(icon = '$\alpha$',prefix = 'fa', color = '$\alpha$'):圖標樣式
 

#### 202108111812