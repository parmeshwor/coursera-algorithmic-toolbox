# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def parenthesis(datali,operatorli,m,M):
    n = len(datali)
    for i in range(n):
        m[i][i] = datali[i]
        M[i][i] = datali[i]

    for j in range(1,n):
        for k in range(n-j):
            g = k+j
            m[k][g],M[k][g] = min_max(k,g,M,m,operatorli)
    return M[0][n-1]

def min_max(i,j,M,m,opli):
    minn =   99999
    maxx =  -99999

    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j],opli[k])
        b = evalt(M[i][k], m[k+1][j],opli[k])
        c = evalt(m[i][k], M[k+1][j],opli[k])
        d = evalt(m[i][k], m[k+1][j],opli[k])
        minn = min(minn,a,b,c,d)
        maxx = max(maxx,a,b,c,d)
    return(minn,maxx)

def get_maximum_value(dataset):

    #write your code here
    # pos of e1 op e2 ; 1 will be pos of exp

    operatorli = dataset[1::2]
    datali = dataset[0::2]
    datali = list(map(int,datali))

    m = [[0]* len(datali) for i in range(len(datali))]
    M = [[0]* len(datali) for i in range(len(datali))]

    return parenthesis(datali,operatorli,m,M)




#print(get_maximum_value('5-8+7*4-8+9'))



if __name__ == "__main__":
    print(get_maximum_value(input()))



