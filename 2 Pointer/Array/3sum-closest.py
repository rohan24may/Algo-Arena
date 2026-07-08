nums = [-1, 2, 1, -4]
target = 1

nums.sort()

closest_sum = nums[0] + nums[1] + nums[2]

for i in range(len(nums)):

    left = i + 1
    right = len(nums) - 1

    while left < right:

        current_sum = nums[i] + nums[left] + nums[right]

        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum

        if current_sum == target:
            print(current_sum)
            exit()

        elif current_sum < target:
            left += 1

        else:
            right -= 1

print(closest_sum)