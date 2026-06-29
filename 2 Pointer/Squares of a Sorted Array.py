# ==========================================================
# SQUARES OF A SORTED ARRAY
# ==========================================================
#
# Given a sorted integer array `nums`, return an array of
# the squares of each number, also sorted in non-decreasing order.
#
# Example:
# Input:  [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
#
# ==========================================================

nums = list(map(int, input("Enter sorted array elements: ").split()))

left = 0
right = len(nums) - 1

answer = [0] * len(nums)
insert = len(nums) - 1

while left <= right:

    if abs(nums[left]) > abs(nums[right]):
        answer[insert] = nums[left] ** 2
        left += 1
    else:
        answer[insert] = nums[right] ** 2
        right -= 1

    insert -= 1

print("Answer:", answer)