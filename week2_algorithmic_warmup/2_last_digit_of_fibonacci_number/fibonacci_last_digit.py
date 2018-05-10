# Uses python3
import sys

def get_fibonacci_last_digit_naive2(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_naive(n):

    table = [0 for i in range(n+2)]
    table[1]=1
    table[0]=0

    if n<=1 :
        return table[n]

    for i in range(2,n+1):
        table[i] = (table[i-1])%10 + (table[i-2])%10

    return (table[n])%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))

    # for n in range(10):
    #     print(get_fibonacci_last_digit_naive(n)==get_fibonacci_last_digit_naive2(n))
