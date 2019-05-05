import random

def bubble_sort(data):
    for i in range(len(data)-1):
        exchange = False
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                exchange = True
        if not exchange:
            break


if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前：',data)
    bubble_sort(data)
    print('排序后：',data)