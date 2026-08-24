class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]

        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            old_max = current_max
            old_min = current_min

            current_max = max(
                nums[i],
                old_max + nums[i],
                old_min + nums[i]
            )

            current_min = min(
                nums[i],
                old_max + nums[i],
                old_min + nums[i]
            )

            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        return max(abs(max_sum), abs(min_sum))