# Uses python3
import sys

def get_change_re(m,min,deno):
    #write your code here

    if m ==0:
        return 0
    if m in deno:
        return 1


    for coin in deno:
        if m>=coin:
            mincoins = get_change_re(m-coin,min,deno)+1

            if min > mincoins:
                min = mincoins
    return min

def get_change_(m,minn,deno,table):
    # base
    if table[m]:
        return table[m]
    else:
        for i in range(5,m+1):
            minn = i
            for coin in deno:
                mincoin = get_change_(i-coin,i,deno,table)+1
                if mincoin < minn:
                    minn = mincoin
            table[i] = minn
        return table[m]

def get_change(m):
    deno = [1,3,4]

    if m<=4:
        if m <=0:
            return 0
        if m==2:
            return 2
        if m in deno:
            return 1
    else :
        minn = m
        table = [False for i in range(m+1)]
        table[0]=0
        table[2]=2
        for i in deno:
            table[i] = 1
        return get_change_(m,minn,deno,table)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 7
    print(get_change(m))



