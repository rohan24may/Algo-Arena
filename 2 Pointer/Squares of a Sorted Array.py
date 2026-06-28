# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

nums = [-4,-1,0,3,10]

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

print(answer)