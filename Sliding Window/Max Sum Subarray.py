class Solution:
    def maxSubarraySum(self, arr, k):

        n = len(arr)

        if n < k:
            return 0

        # Sum of the first window
        window_sum = sum(arr[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum