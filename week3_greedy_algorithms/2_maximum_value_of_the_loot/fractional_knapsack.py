# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0.
    pairs = list(zip(values,weights))
    ratios = sorted(pairs, key= lambda x: x[0]/x[1], reverse=True)



    for (v,w) in ratios:
        #print('iteration',iter, v, w)

        if capacity-w >= 0:
            capacity = capacity - w
            value = value + v

        else:
            partial_wt = capacity
            value = value+v/w * capacity
            break

    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


# capacity = 50
# weights = [20,50,30]
# values = [60,100,120]
#
# print(get_optimal_value(capacity, weights, values))



