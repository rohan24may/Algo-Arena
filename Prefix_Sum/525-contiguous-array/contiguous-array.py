class Solution:
    def findMaxLength(self, nums: List[int]) -> int: # pyright: ignore[reportUndefinedVariable]
        prefix_sum = 0
        max_length = 0
        prefix_map = {0: -1}

        for i, num in enumerate(nums):

            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in prefix_map:
                current_length = i - prefix_map[prefix_sum]
                max_length = max(max_length, current_length)
            else:
                prefix_map[prefix_sum] = i

        return max_length