class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def get_next(i, direction):
            # Check direction
            if (nums[i] > 0) != direction:
                return -1

            # Calculate next index
            next_i = (i + nums[i]) % n

            # Reject 1-element cycle
            if next_i == i:
                return -1

            return next_i

        for i in range(n):
            direction = nums[i] > 0

            slow = i
            fast = i

            while True:
                # Slow moves 1 step
                slow = get_next(slow, direction)

                if slow == -1:
                    break

                # Fast moves 1st step
                fast = get_next(fast, direction)

                if fast == -1:
                    break

                # Fast moves 2nd step
                fast = get_next(fast, direction)

                if fast == -1:
                    break

                # Cycle found
                if slow == fast:
                    return True

        return False