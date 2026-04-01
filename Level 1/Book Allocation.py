def is_possible(arr, students, max_pages):
    count = 1
    pages = 0

    for x in arr:
        if pages + x <= max_pages:
            pages += x
        else:
            count += 1
            pages = x

    return count <= students


def allocate(arr, students):
    low = max(arr)
    high = sum(arr)
    ans = high

    while low <= high:
        mid = (low + high) // 2

        if is_possible(arr, students, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = list(map(int, input().split()))
students = int(input())

print(allocate(arr, students))