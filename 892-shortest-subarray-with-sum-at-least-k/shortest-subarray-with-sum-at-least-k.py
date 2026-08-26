from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        min_length = float('inf')
        dq = deque([(0, 0)])

        for i, num in enumerate(nums, 1):

            prefix_sum += num

            while dq and prefix_sum - dq[0][1] >= k:
                min_length = min(min_length, i - dq[0][0])
                dq.popleft()

            while dq and prefix_sum <= dq[-1][1]:
                dq.pop()

            dq.append((i, prefix_sum))

        return min_length if min_length != float('inf') else -1