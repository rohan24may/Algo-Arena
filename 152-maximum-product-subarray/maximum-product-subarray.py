class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            old_max = max_product
            old_min = min_product

            max_product = max(
                nums[i],
                nums[i] * old_max,
                nums[i] * old_min
            )

            min_product = min(
                nums[i],
                nums[i] * old_max,
                nums[i] * old_min
            )

            answer = max(answer, max_product)

        return answer