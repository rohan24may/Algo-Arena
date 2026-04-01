def first_occ(arr, target):
    low, high = 0, len(arr)-1
    ans = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            ans = mid
            high = mid - 1   # go left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans