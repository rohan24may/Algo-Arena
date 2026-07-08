"""
18. 4Sum

Question:

Given an integer array nums and an integer target,
return all the unique quadruplets:

[nums[a], nums[b], nums[c], nums[d]]

such that:

1. All four indices are different.
2. nums[a] + nums[b] + nums[c] + nums[d] == target.
3. The answer must not contain duplicate quadruplets.

--------------------------------------------------

Example 1:

Input:
nums = [1,0,-1,0,-2,2]
target = 0

Output:
[
    [-2,-1,1,2],
    [-2,0,0,2],
    [-1,0,0,1]
]

Time Complexity : O(n³)
Space Complexity : O(1)
"""

nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()

answer = []

for i in range(len(nums)):

    # Skip duplicate first number
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, len(nums)):

        # Skip duplicate second number
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = len(nums) - 1

        while left < right:

            current_sum = (
                nums[i] +
                nums[j] +
                nums[left] +
                nums[right]
            )

            if current_sum == target:

                answer.append([
                    nums[i],
                    nums[j],
                    nums[left],
                    nums[right]
                ])

                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < target:

                left += 1

            else:

                right -= 1

print(answer)