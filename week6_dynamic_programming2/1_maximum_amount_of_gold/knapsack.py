# Uses python3
import sys

def optimal_weight(W,w):

    col = W
    row = len(w)

    c = [i for i in range(col+1)]
    r = w

    table = [[0]*(col+1) for i in range(row)]
    #print(table)

    # first row
    i = 0
    v = w[0]
    for j in range(col+1):
        if v<=j:
            table[i][j] = v
        else:
            table[i][j] = 0


    for i,val in enumerate(w[1:]):
        i = i+1
        for j in range(col+1):
            # if j ==0:
            #     table[i][j]=table[i][j-1]
            if val>j:
                table[i][j] = table[i-1][j]
            elif val==j:

                table[i][j]=max(val,table[i-1][j])
            elif val < j:
                tmp = j-val
                table[i][j]=max(val + table[i-1][tmp], table[i-1][j])
    #print(table)
    #print(col,row-1)
    return table[row-1][col]

def optimal_weight_(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


# W = 20
# n = 4
# w = [5,7,12,18]
#
# print(optimal_weight(W,w))
