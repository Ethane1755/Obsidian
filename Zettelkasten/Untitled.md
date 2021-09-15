# Untitled
```mermaid
graph TD
subgraph 容器種類
50mL燒杯-->50mL錐形瓶-->吸量管25mL-->容量瓶10mL-->量筒25mL-->滴定管50mL
end
取100mL燒杯置於秤盤上-->測量空燒杯質量-->取容器
subgraph 6次
取容器-->id1(利用容器刻度量測10mL水)
id1-->|5次|id1
end
容器種類-.-取容器
```