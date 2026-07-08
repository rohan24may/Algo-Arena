"""15. 3Sum (Medium)
Question:
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]]
such that:

i != j
i != k
j != k

nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example:

Input:
nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]
"""

nums = [-1,0,1,2,-1,-4]
nums.sort()
# nums = [-4,-1,-1,0,1,2]

answer = []

for i in range(len(nums)):

    # Skip duplicate fixed numbers
    if i > 0 and nums[i] == nums[i-1]:
        continue

    left = i + 1
    right = len(nums) - 1

    target = -nums[i]

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:

            answer.append([nums[i], nums[left], nums[right]])

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