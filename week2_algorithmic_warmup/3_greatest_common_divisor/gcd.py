# Uses python3
import sys

def gcd_naive2(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

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









if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
