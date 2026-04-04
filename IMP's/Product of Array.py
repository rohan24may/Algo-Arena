def product(arr):
    n = len(arr)
    res = [1]*n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]

    return res


arr = list(map(int, input().split()))
print(product(arr))