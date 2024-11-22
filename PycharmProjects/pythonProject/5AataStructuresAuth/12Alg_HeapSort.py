'''
尝试实现堆排序，（允许借助百度搜索）。
'''


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


# 测试代码
if __name__ == "__main__":
    arr = [100, 5, 3, 11, 33, 6, 8, 7]
    print("未排序数组:", arr)
    heap_sort(arr)
    print("已排序数组:", arr)
