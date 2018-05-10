# Uses python3

def edit_distance(s1, s2):
    #write your code here
    r = len(s1) +1
    c = len(s2) +1
    table = [[0]*r for i in range(c)]

    for i in range(r):
        table[0][i] = i

    for j in range(c):
        table[j][0] = j



    for i in range(1,c):
        for j in range(1,r):
            if s1[j-1] == s2[i-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(table[i-1][j],table[i-1][j-1],table[i][j-1]) + 1


    return table[c-1][r-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))


# print(edit_distance('abcdef','agced'))

"""
short-
p-orts
"""
