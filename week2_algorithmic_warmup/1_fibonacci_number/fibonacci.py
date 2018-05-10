# Uses python3

import random

# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)




def calc_fib(n):

    table = [0 for i in range(n+2)]
    table[1]=1
    table[0]=0

    if n<=1 :
        return table[n]

    for i in range(2,n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]


n = int(input())
print(calc_fib(n))
# inputs = [random.randrange(0,5) for i in range(10)]


# for input in inputs:
#     if dynamic_fibo(input) == calc_fib(input):
#         pass
#     else:
#         print(input, dynamic_fibo(input), calc_fib(input), 'Error!!')
