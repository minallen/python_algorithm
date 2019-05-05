import time

# 时间装饰器
def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # print("%s running time: %s secs." % (func.__name__, start_time - end_time))
        print("%s 函数执行时间是: %s 秒" % (func.__name__, start_time - end_time))
        return result

    return wrapper


@cal_time
def bin_search(data_list, val):
    # 开始位置：第0个位置
    low = 0
    # 结束位置：最后一个位置
    high = len(data_list) - 1
    # 循环判断
    while low <= high:
        # 获取中间位置,这里需要整除//
        mid = (low + high) // 2
        # 判断中间索引对应的数字是不是查找的数字
        if data_list[mid] == val:
            #print(data_list[mid])
            return mid
        # 如果中间索引对应的数字在查找数字的左边，则 low = mid + 1
        elif data_list[mid] < val:
            low = mid + 1
        # 如果中间索引对应的数字在查找数字的右边，则  high = mid - 1
        elif data_list[mid] > val:
            high = mid - 1
    return


if __name__ == '__main__':
    data_list = list(range(1,10000))
    ret = bin_search(data_list, 6666)
    print(ret)
