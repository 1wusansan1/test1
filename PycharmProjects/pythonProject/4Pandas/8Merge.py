import pandas as pd
'''
merge函数:
   使用merge()函数， 通过 on 参数指定一个连接键，然后对上述 DataFrame 进行合并操作： 
'''
left = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['Smith', 'Maiki', 'Hunter', 'Hilen'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6']})
right = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['William', 'Albert', 'Tony', 'Allen'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6']})

print(left)
print(right)
#  on='id' 通过id相同的行合并再一起（左右）
print(pd.merge(left, right, on='id'))
