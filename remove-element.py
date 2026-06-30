# Given an integer array nums and an integer val, remove all occurrences of val in-place.

# Return the number of elements that are not equal to val.

# The first k elements should contain the remaining values.

# Example 1
# Input:
# nums = [3,2,2,3]
# val = 3

# Output:
# 2

# nums = [2,2]


def removeElement(nums, val):
    left = 0

    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1

    return left


nums = [3, 2, 2, 3]
val = 3

k = removeElement(nums, val)

print(k)
print(nums[:k])