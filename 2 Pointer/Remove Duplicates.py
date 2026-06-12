# LeetCode 26 - Remove Duplicates from Sorted Array

# Example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5
# nums = [0,1,2,3,4,_,_,_,_,_]

# Pattern: Two Pointers (Slow & Fast)

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1