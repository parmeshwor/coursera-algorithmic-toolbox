# Uses python3
import sys


def naive_majority(a):
    n = len(a)
    for i in a:
        if a.count(i) > n/2:
            return i
    return False

def check_majority(a,m1,m2):
    n = len(a)
    if a.count(m1) > n/2:
        return m1
    if a.count(m2) > n/2:
        return m2

    return False


def get_majority(a,lo,hi):

    if hi - lo <=3:
        return naive_majority(a[lo:hi+1])

    mid = lo + (hi-lo)//2

    maj1 = get_majority(a,lo,mid-1)
    maj2 = get_majority(a,mid,hi)

    # check which one is majority after combine

    return check_majority(a[lo:hi+1],maj1,maj2)

def get_majority_element(a, left, right):

    #write your code here
    majority_element = get_majority(a,left,right-1)
    if majority_element:
        #print('majority_element',majority_element)
        return majority_element
    return -1

# a = [1,2,2,1]
# print(naive_majority(a), get_majority_element(a,0,len(a)))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    #print('----------',n,':::::',a)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
