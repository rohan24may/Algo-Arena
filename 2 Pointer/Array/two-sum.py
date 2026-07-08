# Given an array of integers `nums` and an integer `target`,
# return the indices of the two numbers such that they add
# up to the target.
#
# You may assume that each input has exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example:
#
# Input:
# nums = [2, 7, 11, 15]
# target = 9
#
# Output:
# [0, 1]
#
# Explanation:
# nums[0] + nums[1] = 2 + 7 = 9
# Therefore, the answer is [0, 1].


# Take input from the user
nums = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target: "))

# Dictionary to store numbers we have already seen
seen = {}

# Traverse the array
for i, num in enumerate(nums):
    need = target - num

    # Check if the required number has already been seen
    if need in seen:
        print("Answer:", [seen[need], i])
        break

    # Store the current number and its index
    seen[num] = i