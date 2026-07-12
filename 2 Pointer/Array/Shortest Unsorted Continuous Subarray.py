"""
581. Shortest Unsorted Continuous Subarray

Question:

Given an integer array nums, find the shortest continuous subarray such that
if you sort only this subarray in ascending order, the entire array becomes sorted.

Return the length of this shortest subarray.

Example 1:

Input:
nums = [2,6,4,8,10,9,15]

Output:
5

Explanation:
Sort [6,4,8,10,9]
Result -> [2,4,6,8,9,10,15]

Time Complexity : O(n)

Space Complexity : O(1)
"""

nums = [2,6,4,8,10,9,15]

min_num = float('inf')
max_num = float('-inf')

# Find the minimum misplaced element
for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        min_num = min(min_num, nums[i])

# Find the maximum misplaced element
for i in range(len(nums) - 2, -1, -1):
    if nums[i] > nums[i + 1]:
        max_num = max(max_num, nums[i])

# Array is already sorted
if min_num == float('inf'):
    print(0)
    exit()

# Find left boundary
for i in range(len(nums)):
    if nums[i] > min_num:
        left = i
        break

# Find right boundary
for i in range(len(nums) - 1, -1, -1):
    if nums[i] < max_num:
        right = i
        break

print(right - left + 1)