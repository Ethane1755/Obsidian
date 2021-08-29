# Untitled

```mermaid
graph TD

id1(輸入n)-->id2(如果n=1)-->|O|id3(不是質數)
id2-->|X|id4(製作變數V代表在2與n之間的每個數)
id4-->id5(檢測n/V餘數是否為0)
id5-->|O|id6(不是質數)
id5-->|X|id5
id5-->id7(當所有V都被檢測完後, n/V都不為0)
id7-->id8(是質數)
style 
```
