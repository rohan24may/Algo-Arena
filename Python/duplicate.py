

def containsDuplicate(nums):
    seen = {}

    for num in nums:
        if num in seen:
            return True

        seen[num] = True

    return False

nums = [1,2,3,1]

print(containsDuplicate(nums))