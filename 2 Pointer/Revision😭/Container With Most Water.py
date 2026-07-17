"""
LeetCode 11. Container With Most Water

Question:
You are given an integer array `height` of length n.

There are n vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container that holds
the maximum amount of water.

Return the maximum amount of water a container can store.

Example:
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation:
The container formed by the lines at index 1 and index 8
holds 49 units of water.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maxArea(height):
    left = 0
    right = len(height) - 1

    maxArea = 0

    while left < right:
        width = right - left
        currArea = width * min(height[left], height[right])

        maxArea = max(maxArea, currArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea


