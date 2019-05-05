
li = [1, 5, 4, 2]
target = 3

def func1():
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == target:
                return (i,j)

ret = func1()
print(ret)      #(0, 3)



