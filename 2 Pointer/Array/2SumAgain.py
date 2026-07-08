# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed).

# You may not use the same element twice.

# There is exactly one solution.
# Example 1:
# Input:
# numbers = [2,7,11,15]
# target = 9

# Output:
# [1,2]

numbers = [2, 7, 11, 15]
target = 9

left = 0
right = len(numbers) - 1

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print([left + 1, right + 1])
        break

    elif current_sum > target:
        right -= 1

    else:
        left += 1