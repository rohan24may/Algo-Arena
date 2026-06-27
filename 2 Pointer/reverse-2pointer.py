"""
344. Reverse String

Given an array of characters, reverse the array in-place.

Example:

Input:
["h","e","l","l","o"]

Output:
["o","l","l","e","h"]
"""

nums = ["h", "e", "l", "l", "o"]

left = 0
right = len(nums) - 1

while left < right:

    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1

print(nums)