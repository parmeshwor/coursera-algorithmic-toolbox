# Uses python3
import sys
import random

# def partition3(a, l, r):
#     #write your code here
#     pass
#
# def partition2(a, l, r):
#     x = a[l]
#     j = l;
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j
#
#
# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     #use partition3
#     m = partition2(a, l, r)
#     randomized_quick_sort(a, l, m - 1);
#     randomized_quick_sort(a, m + 1, r);


def partition3(a, lo, hi):
    #write your code here

    pivot = a[hi]

    i = lo - 1
    for j in range(lo,hi):
        if a[j] < pivot:
            i=i+1
            a[i], a[j] = a[j], a[i]
    p1 = i
    for k in range(i+1,hi):
        if a[k] == pivot:
            i = i+1
            a[i], a[k] = a[k],a[i]
    a[i+1] , a[hi] = a[hi], a[i+1]
    p2 = i+2
    return p1,p2





def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    p1,p2 = partition3(a, l, r)
    randomized_quick_sort(a, l, p1);
    randomized_quick_sort(a, p2, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
