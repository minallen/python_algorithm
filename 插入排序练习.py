# import random
#
# def insert_sort(data_list):
#     for i in range(1,len(data_list)):
#         temp = data_list[i]
#         j = i - 1
#         while j>=0 and data_list[j] > temp:
#             data_list[j+1] = data_list[j]
#             j = j - 1
#         data_list[j+1] = temp
#
# if __name__ == '__main__':
#     data_list = list(range(6666))
#     random.shuffle(data_list)
#     print('打乱后的数据\n',data_list)
#     insert_sort(data_list)
#     print('排序后的数据\n',data_list)



import random


def insert_sort(data):
    for i in range(1,len(data)):
        tmp = data[i]
        j = i - 1
        while j>=0 and data[j] >tmp:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = tmp

if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前的数据',data)
    insert_sort(data)
    print('排序后的数据',data)













