# import random
#
# #从小到大排序
# def select_sort(data_list):
#     for i in range(len(data_list)-1):
#         min_index = i
#         for j in range(i+1,len(data_list)):
#             if data_list[min_index] > data_list[j]:
#                 min_index = j
#         data_list[i],data_list[min_index] = data_list[min_index],data_list[i]
#
# if __name__ == '__main__':
#     data_list = list(range(6666))
#     random.shuffle(data_list)
#     print('打乱后的数据\n',data_list)
#     select_sort(data_list)
#     print('排序后的数据\n',data_list)






import random

def select_sort(data):
    for i in range(len(data)-1):
        #假设i对应的值时最小值
        min_index = i
        for j in range(i+1,len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]

if __name__ == '__main__':
    data = list(range(1000))
    random.shuffle(data)
    print('排序前的数据',data)
    select_sort(data)
    print('排序后的数据',data)














