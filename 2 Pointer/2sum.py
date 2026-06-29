# Given a sorted array `numbers` and a target,
# return the 1-based indices of the two numbers
# that add up to the target.
#
# Example:
# Input:  numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]

def twoSum(numbers, target):

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


numbers = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

print("Answer:", twoSum(numbers, target))