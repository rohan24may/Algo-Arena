def search_rotated(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # left sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = list(map(int, input().split()))
target = int(input())
print(search_rotated(arr, target))