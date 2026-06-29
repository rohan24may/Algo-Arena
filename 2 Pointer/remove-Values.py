# Given an integer array `nums` and an integer `val`,
# remove all occurrences of `val` in-place and return
# the number of remaining elements.
#
# Example:
# Input:  nums = [3, 2, 2, 3], val = 3
# Output: Length = 2
# Array: [2, 2]

nums = list(map(int, input("Enter array elements: ").split()))
val = int(input("Enter value to remove: "))

insert_pos = 0

for num in nums:
    if num != val:
        nums[insert_pos] = num
        insert_pos += 1

print("Length:", insert_pos)
print("Array:", nums[:insert_pos])