import random


def select_sort(data_list):
    for i in range(len(data_list) - 1):
        # 假设第i个索引对应的值最小
        min_index = i
        # 第i个索引对应的值 和 从第i+1个索引开始的数进行循环比较
        for j in range(i + 1, len(data_list)):
            if data_list[min_index] > data_list[j]:
                min_index = j
        # 注意：这时 data_list[min_index] = data_list[j]
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]


if __name__ == '__main__':
    data_list = list(range(1001))
    # 打乱数字顺序
    random.shuffle(data_list)
    select_sort(data_list)
    print(data_list)
