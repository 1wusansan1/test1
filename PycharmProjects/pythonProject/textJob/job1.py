
# 构建最大堆
def heapify(arr, n, i):
    """
       将以i为根的子树调整为最大堆
       :param arr: 待调整的数组
       :param n: 数组的长度
       :param i: 根节点的索引
       """
    max = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[max]:
        max = left
    if right < n and arr[right] > arr[max]:
        max = right

    if max != i:  # 说明最大值要与夫进行替换
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, n, max)  # 发生替换后的子节点受影响，继续递归构建

# import torch
# 堆排序
def heap_sort(arr):
    n = len(arr)
    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 替换根节点与最后一个叶子节点，n-1 -> 0 (元素个数减少，后面的最大值固定不变)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # 从0开始重新生成最大堆
        heapify(arr, i, 0)

#
def binary_search(alist, item):
    lens = len(alist)
    if lens == 0:
        return False
    middle = lens // 2
    if alist[middle] < item:
        return binary_search(alist[middle + 1:], item)
    elif alist[middle] > item:
        return binary_search(alist[:middle], item)
    else:
        return True


if __name__ == '__main__':
    # l1 = [10, 80, 30, 60, 50, 40, 70, 20, 90]
    # heap_sort(l1)
    # print(l1)
    # if binary_search(l1, 30):
    #     print('30 in list')
    # else:
    #     print('30 not in list')
    print(2+2+10+12+15+10+18)

