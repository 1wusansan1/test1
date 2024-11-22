import pandas as pd

'''
数据去重: duplicated(),drop_duplicates()
'''
print('======================================================数据去重')
person = {
    "name": ['Google', 'baidu', 'baidu', 'Taobao', 'baidu'],
    "age": [50, 40, 40, 23, 40]
}

df = pd.DataFrame(person)
print(df)
print(df.duplicated())
df.drop_duplicates(inplace=True)

# 要使用drop_duplicates函数的subset参数去重，针对name这一列去重
# df = df.drop_duplicates(subset=['name'])
print(df)
