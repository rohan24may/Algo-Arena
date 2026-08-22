class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        normal_sum = arr[0]
        deleted_sum = float("-inf")
        max_sum = arr[0]

        for i in range(1, len(arr)):
            old_normal = normal_sum

            deleted_sum = max(
                deleted_sum + arr[i],
                old_normal
            )

            normal_sum = max(
                arr[i],
                old_normal + arr[i]
            )

            max_sum = max(
                max_sum,
                normal_sum,
                deleted_sum
            )

        return max_sum