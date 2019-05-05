import random


def insert_sort(data):
    for i in range(1,len(data)):
        tmp = data[i]
        j = i - 1
        #前一个数字比现在的数字大的时候
        while j >= 0 and data[j] > tmp:
            #往后移动一个位置
            data[j+1] = data[j]
            #循环取看前一个位置上的数字
            j = j - 1
        data[j+1] = tmp

if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前：',data)
    insert_sort(data)
    print('排序后：',data)

