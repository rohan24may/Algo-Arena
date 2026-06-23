# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Note:
# - You must do this in-place without making a copy of the array.

# Example 1:

# Input:
# nums = [0,1,0,3,12]

# Output:
# [1,3,12,0,0]

nums = [0,1,0,3,12]

def moveZeroes(nums):

    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0

    return nums

print(moveZeroes(nums))
