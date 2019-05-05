# import random
#
# #从小到大排列
# def bubble_sort(data_list):
#     for i in range(len(data_list)-1):
#         exchange = False
#         for j in range(len(data_list)-1-i):
#             if data_list[j] > data_list[j+1]:
#                 data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
#                 exchange = True
#         if not exchange:
#             break
#
# if __name__ == '__main__':
#     data_list = list(range(6000))
#     random.shuffle(data_list)
#     print('打乱后的数据\n',data_list)
#     bubble_sort(data_list)
#     print('排序后的数据\n',data_list)








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
    data = list(range(100))
    random.shuffle(data)
    print('打乱后',data)
    bubble_sort(data)
    print('排序后',data)













