# Given a sorted array `nums`, remove the duplicates
# in-place so that each unique element appears only once.
#
# Return the number of unique elements.
#
# Example:
# Input:  [0,0,1,1,1,2,2,3,3,4]
# Output: Length = 5
# Array: [0,1,2,3,4]

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


nums = list(map(int, input("Enter sorted array elements: ").split()))

k = removeDuplicates(nums)

print("Length:", k)
print("Array:", nums[:k])