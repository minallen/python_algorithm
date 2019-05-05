import random


def quick_sort(data, left, right):
    if left < right:
        # mid = left
        mid = partition(data, left, right)

        # 左边递归
        quick_sort(data, left, mid - 1)
        # 右边递归
        quick_sort(data, mid + 1, right)


def partition(data, left, right):
    tmp = data[left]

    while left < right:
        # 从右边开始循环
        # while left < right and data[right] >= tmp:
        while left < right and data[right] <= tmp:
            right = right - 1
        data[left] = data[right]

        # 从左边开始循环
        # while left < right and data[left] <= tmp:
        while left < right and data[left] >= tmp:
            left = left + 1
        # 填补right的空位置,left的位置空了
        data[right] = data[left]

    # 当 left 出现 大于等于 right时，找到了tmp 的真正位置，结束循环
    data[left] = tmp
    return left


if __name__ == '__main__':
    data = list(range(1,10086))
    #data = [1,5,9,2,8,6,7]
    random.shuffle(data)
    print('排序前：', data)
    quick_sort(data, 0, len(data) - 1)
    print('排序后', data)
