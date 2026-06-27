nums = [3,2,2,3]
val = 3

insert_pos = 0

for num in nums:

    if num != val:

        nums[insert_pos] = num
        insert_pos += 1

print(nums)
print(insert_pos)