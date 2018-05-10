# Uses python3
# 10 2 3 4 5 6 7 8 9 10 11 12 1 2 3 4 5 6 7 8 9 10 11 12
import sys
import random

def binary_search2(a, x, left, right):
    #left, right = 0, len(a)
    # right = len(a)

    if left > right :
        return -1
    mid = left+ (right-left) // 2

    # print('low mid hi',left, mid, right)
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search2(a, x, left,mid-1)
    elif x > a[mid]:
        return binary_search2(a,x,mid+1,right)
    return -1

def binary_search(a,x):

    return binary_search2(a,x, 0,len(a)-1)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


#
# for i in  range(10):
#     a = sorted(random.sample(range(0,100),10))
#     print(a)
#
#     x = a[5]
#     print(x,'::::', a)
#     print('RESULT ::',binary_search(a,x), linear_search(a,x),binary_search(a,x)== linear_search(a,x))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

#
# print(binary_search([2,3,4,5,6,7,8,9,10,11],12))
