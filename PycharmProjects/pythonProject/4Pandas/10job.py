import pandas as pd
from matplotlib import pyplot as plt

# 设置使中文显示完整
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

'''
# 通过pandas加载数据集，并将其中‘time’列转换为整数形式。按照'time'列实现去重操作
#（提示：要使用drop_duplicates函数的subset参数）并把去重后的数据，按照年份为x轴，收益为y轴的形式画出折线图。效果如下图所示。
'''
df = pd.read_csv("BondYield.csv")

# 并将其中‘time’列转换为整数形式
df['time'] = df['time'].astype(int)

# 要使用drop_duplicates函数的subset参数去重
df = df.drop_duplicates(subset=['time'])

# time设为行索引
indexs = df['time'].values
indexs = indexs.astype(str)
df.index = indexs

del df['rownames']
del df['time']
print(df)
df.plot(color='red')
plt.title("收益率统计图")
plt.show()
