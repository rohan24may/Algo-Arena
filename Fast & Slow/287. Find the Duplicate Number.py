class Solution:
    def findDuplicate(self, nums: List[int]) -> int: # pyright: ignore[reportUndefinedVariable]

        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find cycle entrance (duplicate number)
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow