#%% 
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み

# data frame
df = pd.read_csv('sample.csv')
df.head(3)

# データの抽出
x = df['x']
y = df['y']

# 散布図
plt.scatter(x, y)
plt.show()

# データの中心化

## データの概要
df_c = df - df.mean()
df_c.head(3)

df_c.describe()

x = df_c['x']
y = df_c['y']
plt.scatter(x, y)
plt.show()

# パラメータaの計算
xx = x * x
xy = x * y

a = xy.sum() / xx.sum()
print(a)

# パラメータaをプロット
plt.scatter(x, y, label='y')
plt.plot(x, a*x, label='y_hat', color="red")
plt.legend() # 凡例の表示
plt.show()

## ここまでが学習フェーズ

# 予測値の計算

x_new = 40
mean = df.mean()
xc = x_new - mean['x']

# 単回帰分析による予測
yc = a * xc
# 予測値
y_hat = a * xc + mean['y']

def predict(x):
  a = 10069.022519284063
  xm = 37.62222
  ym = 121065.00000
  # 中心化
  xc = x - xm
  y_hat = a * xc + ym
  return y_hat

# 内挿
print(predict(40))
# 外挿
print(predict(25))
