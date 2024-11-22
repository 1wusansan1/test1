import random

'''
算法：
    1） 从待排序序列中任意挑选一个元素，作为基准 
    2）将所有小于基准的元素放在基准之前，大于基准的元素放在基准之后，等于基准的元素放在基准之前或之后，这个过程称为分组 
    3）以递归的方式，分别对基准之前和基准之后的分组继续进行分组，直到每个分组内的元素个数不多于 1个——自然有序——为止
特点：
    平均时间复杂度：O(NlogN)
    空间复杂度：O(log n) ，  使用递归调用的堆栈空间 
    非稳定排序
'''


def quick_sort(alist, start, end):
    if start >= end:  # 递归结束条件
        return

    # 找一个基准值
    std_index = (start + end) // 2
    std_val = alist[std_index]

    low = start
    high = end
    # 找基准，完成一次左边小值，右边大值的循环归并，
    while low < high:  # 将传入要排序的列表分为了基准值的左右两侧
        while low < high and alist[low] < std_val:
            low += 1
        alist[std_index] = alist[low]  # 左侧的值往右挪
        std_index = low

        while low < high and alist[high] >= std_val:
            high -= 1
        alist[std_index] = alist[high]  # 右侧的值往左挪
        std_index = high
    alist[std_index] = std_val  # 循环之后，基准值回填
    # 之后，左右的子集继续循环归并，直到每个分组内的元素个数不多于 1个——自然有序——为止
    quick_sort(alist, start, std_index - 1)
    quick_sort(alist, std_index + 1, end)


if __name__ == '__main__':
    # l1 = [10,80,30,60,50,40,70,20,90]
    l1 = [10, 20, 30, 40, 50, 60]
    # l1 = [random.randint(0, 100) for i in range(10)]
    print("排序前: ", l1)
    quick_sort(l1, 0, len(l1) - 1)
    print('排序后: ', l1)
