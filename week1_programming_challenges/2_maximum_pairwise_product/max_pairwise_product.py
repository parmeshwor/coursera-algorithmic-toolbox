# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)

result = 0

# done by default
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]


if a[0] >= a[1]:
    max1 = a[0]
    max2 = a[1]
else:
    max1 = a[1]
    max2 = a[0]
#print('first', max1,max2)
for i in range(2,n):

    if a[i] > max1:
        max2 = max1
        max1 = a[i]

    elif a[i] > max2:
        max2 = a[i]
    # print(i,a[i], max1, max2)

result = max1 * max2

print(result)
