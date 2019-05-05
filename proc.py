# list1 = [1,2,3]
#
# high = len(list1) -1
# #print(high)
#
#
# li = [3,2,1]
# #print(len(li))
#
# a = [3,2,1]
# min_index=0
#
# for i in range(len(a)-1):   #0,1,2
#     min_index = i
#     #print(min_index)
#
# l = [99,88,77]
# # print(len(l))
# # print(l[1])
#
#
# print(range(10,1,-1))


#
# count = [0]
# count = count * 3
# print(count)
# import random
#
# def insert_sort(li):
#     for i in range(1, len(li)):
#         temp = li[i]
#         j = i - 1
#         while j >= 0 and li[j] > temp:
#             li[j + 1] = li[j]
#             # 少了一个数
#             j = j - 1
#         li[j + 1] = temp
#
#
# # k 是 个数
# def topk(li, k):
#     # 多开一个空间，所以是 k + 1
#     ltmp = li[0:k + 1]
#     # 这里调用一下插入排序
#     insert_sort(ltmp)
#     for i in range(k + 1, len(li)):
#         ltmp[k] = li[i]
#         tmp = ltmp[k]
#         j = i - 1
#         while j >= 0 and ltmp[j] > tmp:
#             tmp[j + 1] = ltmp[j]
#             j = k - 1
#         ltmp[j + 1] = tmp
#     return ltmp
#
#
# if __name__ == '__main__':
#     li = list(range(1000))
#     random.shuffle(li)
#     print(topk(li, 10))
#
#
#




import random

# def insert(li, i):
#     tmp = li[i]
#     j = i - 1
#     while j >= 0 and li[j] > tmp:
#         li[j + 1] = li[j]
#         j = j - 1
#     li[j + 1] = tmp
#
# def insert_sort(li):
#     for i in range(1, len(li)):
#         insert(li, i)
#
#
# def topk(li, k):
#     top = li[0:k + 1]
#     insert_sort(top)
#     for i in range(k+1, len(li)):
#         top[k] = li[i]
#         insert(top, k)
#     return top[:-1]
#
#
# if __name__ == '__main__':
#     li = list(range(1000))
#     random.shuffle(li)
#     print(topk(li, 10))






def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:    #孩子在堆里
        if j + 1 <= high and data[j] < data[j+1]:   #如果有右孩子且比左孩子大
        #if j + 1 <= high and data[j] > data[j+1]:   #如果有右孩子且比左孩子大
            j += 1  #j指向右孩子
        if data[j] > tmp:   #孩子比最高领导大
        #if data[j] < tmp:   #孩子比最高领导大
            data[i] = data[j]   #孩子填到父亲的空位上
            i = j               #孩子成为新父亲
            j = 2 * i +1        #新孩子
        else:
            break
    data[i] = tmp           #最高领导放到父亲位置


def topn(li, n):
    heap = li[0:n]
    for i in range(n // 2 - 1, -1, -1):
        sift(heap, i, n - 1)
    #遍历
    for i in range(n, len(li)):
        if li[i] < heap[0]:
            heap[0] = li[i]
            sift(heap, 0, n - 1)
    for i in range(n - 1, -1, -1):  # i指向堆的最后
        heap[0], heap[i] = heap[i], heap[0]  # 领导退休，刁民上位
        sift(heap, 0, i - 1)  # 调整出新领导
    return heap

data = list(range(10000))
random.shuffle(data)
print(topn(data, 10))

