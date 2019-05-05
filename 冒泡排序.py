import random


def buble_sort1(data_list):
    # i 是已经执行的趟数 i=n-1 ,n是列表中数字总个数=len(data_list)
    for i in range(len(data_list) - 1):
        # j是等待执行的趟数
        for j in range(len(data_list) - 1 - i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]


#优化
#如果排了一半，后面数据不需要排序的情况
def buble_sort2(data_list):
    # i 是已经执行的趟数 i=n-1 ,n是列表中数字总个数=len(data_list)
    for i in range(len(data_list) - 1):
        exchange = False
        # j是等待执行的趟数
        for j in range(len(data_list) - 1 - i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                #如果进行交换，则修改变量
                exchange = True
        #如果没发生交换
        if not exchange:    #exchange = False
            break




if __name__ == '__main__':
    data_list = list(range(1001))
    # 打乱数字顺序
    random.shuffle(data_list)
    # print(data_list)
    buble_sort2(data_list)
    print(data_list)
