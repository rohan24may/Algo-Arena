def permute(arr, index):
    if index == len(arr):
        print(arr)
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]

        permute(arr, index+1)

        arr[index], arr[i] = arr[i], arr[index]


arr = list(map(int, input().split()))
permute(arr, 0)