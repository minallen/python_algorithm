import random


def insert_sort(data_list):
    for i in range(1, len(data_list)):
        temp = data_list[i]
        j = i - 1
        while j >= 0 and data_list[j] > temp:
            data_list[j + 1] = data_list[j]
            # 少了一个数
            j = j - 1
        data_list[j + 1] = temp


if __name__ == '__main__':
    data_list = list(range(1001))
    # 打乱数字顺序
    random.shuffle(data_list)
    # print(data_list)
    insert_sort(data_list)
    print(data_list)
