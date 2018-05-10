# Uses python3
import sys

def lcm_naive2(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_naive(a,b):

    num = den = 0
    if a > b:
        num = a
        den = b
    else:
        num = b
        den = a

    rem = 1
    quo = 1


    while rem != 0:

        rem = num % den
        quo = num // den

        num = den
        den = rem
    return num

def lcm_naive(a,b):

    gcd = gcd_naive(a,b)

    return a * b // gcd


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

