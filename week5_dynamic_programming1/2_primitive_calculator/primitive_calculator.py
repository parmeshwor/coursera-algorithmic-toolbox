# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:

            n = n // 2

        else:
            n = n - 1
    return len(sequence)

def recur(n):

    if n in [1,2,3]:
        return 1
    elif n==0:
        return 0

    else:
        minval = n

        if (n%3==0 ):
            minval_3 = recur(n//3)+1
            minval = min(minval,minval_3)
        if (n%2==0 ):
            minval_2 = recur(n//2)+1
            minval = min(minval,minval_2)
        if n-1 >= 0:
            minval_1 = recur(n-1)+1
            minval = min(minval,minval_1)

        return minval

def dyna(n):

    if n in [1,2,3]:
        return 1
    elif n==0:
        return 0

    else:
        minval = n

        if (n%3==0 ):
            minval_3 = dyna(n//3)+1
            minval = min(minval,minval_3)
        if (n%2==0 ):
            minval_2 = dyna(n//2)+1
            minval = min(minval,minval_2)
        if n-1 >= 0:
            minval_1 = dyna(n-1)+1
            minval = min(minval,minval_1)

        return minval

x = set()
val = 96234

def solve(n):
  v = [0]*(n+1)  # so that v[n] is there
  v[1] = 1  # length of the sequence to 1 is 1
  for i in range(1,n+1):
    v[i] = v[i-1]+1
    if i%2==0: v[i] = min (v[i],v[i//2]+1)
    if i%3 == 0 : v[i] = min(v[i],v[i//3]+1)

  solution = []
  while n > 1:
    solution.append(n)
    if v[n-1] == v[n] - 1: n = n-1
    elif n%2 == 0 and v[n//2] == v[n] -1: n = n//2
    elif n%3 == 0 and v[n//3] == v[n]-1 : n= n//3
  solution.append(1)
  return reversed(solution)

#print(dyna(val),dyna(val)==optimal_sequence(val),optimal_sequence(val))

input = sys.stdin.read()
n = int(input)
sequence = list(solve(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')





