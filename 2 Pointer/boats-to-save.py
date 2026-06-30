# Problem

# You are given an array people where people[i] is the weight of the i-th person, and an integer limit.

# Each boat can carry at most 2 people, and the total weight cannot exceed limit.

# Return the minimum number of boats needed.

# Example 1
# Input:
# people = [1,2]
# limit = 3

# Output:
# 1

# Explanation:

# 1 + 2 = 3

def numRescueBoats(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1

    boats = 0

    while left <= right:

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


print(numRescueBoats([3,2,2,1], 3))
print(numRescueBoats([3,5,3,4], 5))