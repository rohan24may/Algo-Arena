"""
169. Majority Element

Given an array nums of size n,
return the element that appears more than n/2 times.

Example:
nums = [2,2,1,1,1,2,2]

Output:
2
"""

nums = [2, 2, 1, 1, 1, 2, 2]


def majority(nums):
    freq = {}

    # Count frequency of each number
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    print("Frequency Dictionary:", freq)

    limit = len(nums) / 2

    print("n =", len(nums))
    print("n/2 =", limit)

    # Find majority element
    for key in freq:
        print(f"Checking {key} -> frequency = {freq[key]}")

        if freq[key] > limit:
            print(f"{key} appears more than n/2 times")
            return key


answer = majority(nums)

print("Majority Element =", answer)