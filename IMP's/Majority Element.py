def majority(arr):
    count = 0
    candidate = None

    for x in arr:
        if count == 0:
            candidate = x
        count += (1 if x == candidate else -1)

    return candidate


arr = list(map(int, input().split()))
print(majority(arr))