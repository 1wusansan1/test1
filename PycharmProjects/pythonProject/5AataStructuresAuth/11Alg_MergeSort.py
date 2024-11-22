import random

'''
归并排序 
算法：
    1）分配合并序列，其大小为两个有序序列大小之和 
    2）设定两个索引变量，分别指向两个有序序列的首元素 
    3） 比较索引目标，较小者进入合并序列，索引后移 
    4） 重复步骤3），直到某一索引到达序列末尾 
    5） 将另一序列的剩余元素直接复制到合并序列末尾
特点：
    时间复杂度：O(NlogN)
    空间复杂度：O(n) 
    稳定排序
    对数据的有序性不敏感
    归并排序也是一种分而治之的排序算法，它的时间复杂度始终为O(n log n)，但它
    需要额外的O(n)空间来存储临时数组。
'''


def merge(left, right):
    l, r = 0, 0  # 记录left  right两个列表的操作索引位置
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) // 2

    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])

    return merge(left, right)


if __name__ == '__main__':
    # l1 = [10,80,30,60,50,40,70,20,90]
    # l1 = [10, 20, 30, 50, 40]
    l1 = [random.randint(0, 100) for i in range(10)]
    print("排序前: ", l1)
    l1 = merge_sort(l1)
    print('排序后: ', l1)
