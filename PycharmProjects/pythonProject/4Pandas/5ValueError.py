import pandas as pd

# 第三个日期格式错误
data = {
    "Date": ['2020/12/01', '2020/12/02', '20201226'],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

print(df)
#  转成datetime
df['Date'] = pd.to_datetime(df['Date'], format='mixed')  # format='mixed' 数据是混合型日期格式
print("********************************************************************************to_datetime")
print(df)

print("********************************************************************************for")

person = {
    "name": ['Google', 'baidu', 'Taobao'],
    "age": [50, 200, 12345]
}

df = pd.DataFrame(person)
print(df)

print(df.index)

for x in df.index:
    if df.loc[x, 'age'] > 100:
        df.loc[x, 'age'] = 20
print(df)
