# ==========================================================
# REMOVE DUPLICATES FROM SORTED ARRAY II
# ==========================================================
#
# Given a sorted array `nums`, remove duplicates in-place
# so that each element appears at most twice.
#
# Return the number of remaining elements.
#
# Example:
# Input:  [1, 1, 1, 2, 2, 3]
# Output: Length = 5
# Array: [1, 1, 2, 2, 3]
#
# ==========================================================

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k


nums = list(map(int, input("Enter sorted array elements: ").split()))

k = removeDuplicates(nums)

print("Length:", k)
print("Array:", nums[:k])