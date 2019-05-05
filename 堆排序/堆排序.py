import random

def sift(data,low,high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        #if j < high and data[j] < data[j + 1]:
        if j < high and data[j] > data[j + 1]:
            j = j + 1
        #if tmp < data[j]:
        if tmp > data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp




def heap_sort(data):
    n = len(data)  # 把堆的长度存一下

    # 建堆：
    # 从最后一个有孩子的父亲开始，直到第一个领导【(n // 2 - 1,-1)--->范围，最后一个 -1是步长】
    # 实验证明：最后一个有孩子的父亲的位置是n // 2 - 1
    for i in range(n // 2 - 1, -1,-1):

    # 每次调整这个领导（'i'）所在的堆【每个小堆做调整】,调整到堆的最后，所以 high = n-1
    # 堆就建好了
        sift(data, i, n - 1)

    # 挨个出数：
    for i in range(n - 1, -1):
        # i 是堆的最后一个元素
        # 领导退休，平民上位
        data[0], data[i] = data[i], data[0]
        # 调整出新领导
        sift(data, 0, i - 1)



if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前：',data)
    heap_sort(data)
    print('排序后：',data)
