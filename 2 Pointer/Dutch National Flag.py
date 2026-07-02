"""
75. Sort Colors (Dutch National Flag Algorithm)

Question:

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent.

We use:
0 → Red
1 → White
2 → Blue

Sort the array in the order:

0s → 1s → 2s

Rules:
- Do NOT use the library sort() function.
- Solve it in ONE PASS.
- Use only O(1) extra space.

--------------------------------------------------

Example 1:

Input:
nums = [2,0,2,1,1,0]

Output:
[0,0,1,1,2,2]

--------------------------------------------------

Example 2:

Input:
nums = [2,0,1]

Output:
[0,1,2]

--------------------------------------------------

Time Complexity: O(n)
Space Complexity: O(1)
"""

nums = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
high = len(nums) - 1

while mid <= high:

    if nums[mid] == 0:

        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1

    elif nums[mid] == 1:

        mid += 1

    elif nums[mid] == 2:

        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

print(nums)