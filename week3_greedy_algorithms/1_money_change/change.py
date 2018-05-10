# Uses python3
import sys

def get_change(m):
    #write your code here

    # 5
    c1 = m //10
    rem1 = m % 10
    c2 = rem1//5
    c3 = rem1 % 5
    return c1+c2+c3

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


# print(get_change(28))
