# LeetCode 167 - Two Sum II (Input Array Is Sorted)

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# Pattern: Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]

            elif curr_sum < target:
                left += 1

            else:
                right -= 1