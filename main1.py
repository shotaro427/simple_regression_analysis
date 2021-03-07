#%%
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 3.9, 6.1])


## データの中心化
x.mean()
y.mean()

xc = x - x.mean()
yc = y - y.mean()

## パラメータaの計算
## 要素ごとの掛け算
xx = xc*xc
xy = xc*yc

xx.sum()
xy.sum()

a = xy.sum() / xx.sum()
print(a)