import pylab as pl                                       # 导入pylab模块
import pandas as pd
import numpy as  np

x = [1, 2, 3, 4, 5, 6, 7, 8]                                                # 横轴数据
y = [122.3, 564.4, 1234.5, 1723.6, 2236.8, 2987.2, 3726.3, 4435.6]          # 纵轴数据

pl.figure(figsize=(8,5))                                                # 调整图片大小
pl.plot(x, y, label='market value', color="b", markerfacecolor="red", marker='o', linewidth=1)       # 绘制折线图
pl.title("L Corporation Market Value(from 2038-2044)")   # 标题
pl.xlabel('Time(Unit:year)')                                        # 标明横轴意义
pl.ylabel('Market Value(Unit:100,000,000$)')             # 标明纵轴意义
for a, b in zip(x, y):                                   # 添加这个循坏显示坐标
    pl.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)  # type: ignore

pl.show()                                                # 显示折线图

df = pd.DataFrame(np.random.random(size=(2, 5)))
fig = df.plot()
fig.figure.savefig('pic.png') # 保存
