import random



def quick_sort(data,left,right):
    if left < right:
        # mid = left
        mid = partition(data,left,right)

        #左边递归
        quick_sort(data,left,mid-1)

        #右边递归
        quick_sort(data,mid+1,right)



def partition(data,left,right):
    tmp = data[left]

    while left < right:

        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]

        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]

    data[left] = tmp

    return left


if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前：', data)
    quick_sort(data, 0, len(data) - 1)
    print('排序后', data)



