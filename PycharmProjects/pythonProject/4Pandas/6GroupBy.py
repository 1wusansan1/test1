import pandas as pd
import numpy as np

data = {'name': ['John', 'Helen', 'Sona', 'Ella', 'John'],
        'score': [82, 98, 91, 87, 100],
        'option_course': ['C#', 'Python', 'Java', 'C', 'JS']}
df = pd.DataFrame(data)
print(df)
# 按照name分组
g = df.groupby('name')
print(g)

#根据对应组的数据值，选择一个组
print(g.get_group('John'))

# 对score计算聚合之后的平均值，最大值
result = g['score'].agg((np.mean, np.max))

print(result)
