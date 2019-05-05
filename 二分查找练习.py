# def bin_search(data,val):
#     low = 0
#     high = len(data) - 1
#     while low <= high:
#         mid = (low+high) // 2
#         if data[mid] == val:
#             return mid
#         elif data[mid] < val:
#             low = mid + 1
#         elif data[mid] > val:
#             high = mid - 1
#     return
#
# if __name__ == '__main__':
#     import random
#     data = [2,3,5,1,6,7,9]
#     r = bin_search(data,7)
#     print('查找数字的索引是：',r)


#二分查找返回范围
def bin_search(data,val):
    low = 0
    high = len(data) - 1
    while low < high:
        mid = (low + high) // 2
        if data[mid] == val:

            left = mid
            right = mid

            while  left >= 0 and data[left] == val:
                left = left -  1
                left = abs(left)

            while right < len(data) and data[right] == val:
                right +=1

            return (left+1,right-1)

        elif data[mid] < val:
            low = mid + 1

        elif data[high] > val:
            high = mid - 1
    return

if __name__ == '__main__':
    data = [1,2,3,3,3,5,5,6,6]
    ret = bin_search(data,2)
    print(ret)























