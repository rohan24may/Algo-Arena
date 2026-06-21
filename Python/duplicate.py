nums = [1,2,3,4]

def containsDuplicate(nums):
    freq={}

    for num in nums:
        if num in freq :
            return True
        else:
            freq[num]=1
    return False

print (containsDuplicate(nums))
