class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]: # pyright: ignore[reportUndefinedVariable]
        stack = []
        ans = [-1] * len(nums)

        for i in range(2 * len(nums)):
            index = i % len(nums)

            while stack and nums[index] > nums[stack[-1]]:
                ans[stack[-1]] = nums[index]
                stack.pop()

            stack.append(index)

        return ans