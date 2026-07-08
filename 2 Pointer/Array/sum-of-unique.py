# You are given an integer array `nums`.
#
# The unique elements of an array are the elements that
# appear exactly once in the array.
#
# Return the sum of all the unique elements of `nums`.
#
# Example 1:
#
# Input:
# nums = [1, 2, 3, 2]
#
# Output:
# 4
#
# Explanation:
# The unique elements are [1, 3], and their sum is 4.



def sumOfUnique(nums):
    freq = {}
    total = 0

    # Count the frequency of each number
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Add only the unique numbers
    for num in nums:
        if freq[num] == 1:
            total += num

    return total


# Take input from the user
nums = list(map(int, input("Enter array elements separated by space: ").split()))

# Print the answer
print("Answer:", sumOfUnique(nums))