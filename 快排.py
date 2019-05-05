import random


def quick_sort_x(data, left, right):
    #判断left right，如果相等，就结束函数
    if left < right:
        #mid是tmp的索引位置
        mid = partition(data, left, right)
        #左边递归
        quick_sort_x(data, left, mid - 1)
        #右边递归
        quick_sort_x(data, mid + 1, right)

def partition(data, left, right):
    #把data[left]赋值给了tmp,所以现在left的位置是空的
    tmp = data[left]
    # 判断left right，如果相等，就结束函数
    while left < right:
        #先从右边开始找
        #右边寻找的是比tmp小的数，所以，如果找到比tmp大的数，进行循环
        while left < right and data[right] >= tmp:
            right -= 1
        # 把右边找到的数赋值给左边，右边出现了空位置
        # 现在指针现在到了左边
        data[left] = data[right]
        # 左边寻找的是比tmp大的数，所以，如果找到比tmp小的数，进行循环
        while left < right and data[left] <= tmp:
            left += 1
        # 把左边找到的数赋值给右边，左边出现了空位置
        # 现在指针现在到了右边
        data[right] = data[left]
    #把tmp赋值给左边空出的位置
    data[left] = tmp
    # 返回tmp的下角标（索引）
    return left


if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前：',data)
    quick_sort_x(data,0,len(data)-1)
    print('排序后：',data)

