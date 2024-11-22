import random

'''
选择排序 
    算法：
        1） 在整个序列中寻找最小元素，与首元素交换 
        2） 在剩余序列中寻找最小元素，与次元素交换 
        3） 以此类推，直到剩余序列中仅包含一个元素
    特点：
        平均时间复杂度：O(n²  )
        空间复杂度：O(1) 
        非稳定排序 
        对数据的有序性不敏感 
        交换次数少，优于冒泡排序
'''


def select_sort(alist):
    n = len(alist)

    for j in range(n - 1):
        min_index = j  # 先假设最小项的下标
        # 把最小的值挪到第一位，循环一次挪一个
        for i in range(j + 1, n): # 这里i循环根据j循环挪动的个数开始递归（j递归几次前面几个已经是最小值了）
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    # l1 = [30,20,50,40,10]
    # l1 = [10, 20, 30, 50, 40]
    l1 = [random.randint(0, 100) for i in range(10)]
    print("排序前: ", l1)
    select_sort(l1)
    print('排序后: ', l1)
