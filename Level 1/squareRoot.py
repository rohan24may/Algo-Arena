def sqrt_n(n):
    low, high = 0, n
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


n = int(input("Enter number: "))
print(sqrt_n(n))