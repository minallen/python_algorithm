import random


def select_sort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1,len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]

if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前：',data)
    select_sort(data)
    print('排序后：',data)