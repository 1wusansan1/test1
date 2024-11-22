import random

'''
排序算法（英语：Sorting algorithm）是一种能将一串数据依照特定顺序进行排列的一种算法。
'''

'''
1.冒泡排序 
    算法：
        1)相邻元素两两比较，前者大于后者，彼此交换 
        2)从第一对到最后一对，最大的元素沉降到最后 
        3)针对未排序部分，重复以上步骤，沉降次大值 
        4)每次扫描越来越少的元素，直至不再发生交换
'''


def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):  # n个数最大需要排序n-1次
        flag = 0  # 该趟比较未产生交换
        # 循环一次把1个最大的值换到了最右面
        for i in range(n - 1 - j):  # 这里根据j的次数减少i循环次数（j递归几次后面几个已经是最大值了）
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                flag = 1  # 产生了交换
        print(f'第{j + 1}趟:', alist)
        if flag == 0:  # 如果未产生交换证明已经是有序的，可以直接返回，不用接着排序
            return


'''
特点：
    平均时间复杂度：O(n² )
    空间复杂度：O(1) 
    稳定排序 : 相等的数排序完之后前后顺序未变化
    对数据的有序性非常敏感 
'''

if __name__ == '__main__':
    # l1 = [30,20,50,40,10]
    # l1 = [10, 20, 30, 50, 40]
    l1 = [random.randint(0, 100) for i in range(10)]
    print("排序前: ", l1)
    bubble_sort(l1)
