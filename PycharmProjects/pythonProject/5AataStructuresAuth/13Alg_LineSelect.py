import random

'''
线性查找 :
    从头开始，依次将每一个元素与查找目标进行比较。或者找到目标，或者找不到目标。
特点：
    时间复杂度：O(n)
    对数据的有序性没有要求
'''
def line_search(alist, item):
    for i in alist:
        if i == item:
            return True
    return False  # 未找到


if __name__ == "__main__":
    li = [random.randint(0, 100) for i in range(10)]
    print(li)
    if line_search(li, 30):
        print('30 in list')
    else:
        print('30 not in list')
