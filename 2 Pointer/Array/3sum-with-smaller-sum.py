"""
Count Triplets With Sum Smaller Than Target

Question:
Given an array of distinct integers and a target sum,
find the number of triplets (i, j, k) such that:

    i < j < k

and

    arr[i] + arr[j] + arr[k] < target

Example 1:
Input:
arr = [-2, 0, 1, 3]
target = 2

Output:
2

Explanation:
The valid triplets are:
(-2, 0, 1)
(-2, 0, 3)

------------------------------------------------

Example 2:
Input:
arr = [5, 1, 3, 4, 7]
target = 12

Output:
4
"""

arr = [-2, 0, 1, 3]
target = 2

arr.sort()

count = 0

for i in range(len(arr)):

    left = i + 1
    right = len(arr) - 1

    while left < right:

        current_sum = arr[i] + arr[left] + arr[right]

        if current_sum < target:

            count += (right - left)
            left += 1

        else:

            right -= 1

print("Total Triplets:", count)