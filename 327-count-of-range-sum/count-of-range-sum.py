class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        # Build prefix sum
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        # Merge Sort function
        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid, right)

            # Count valid pairs
            k = mid
            j = mid

            for i in range(left, mid):

                while k < right and prefix[k] - prefix[i] < lower:
                    k += 1

                while j < right and prefix[j] - prefix[i] <= upper:
                    j += 1

                count += j - k

            # Merge the two sorted halves
            merged = []
            p1 = left
            p2 = mid

            while p1 < mid and p2 < right:
                if prefix[p1] <= prefix[p2]:
                    merged.append(prefix[p1])
                    p1 += 1
                else:
                    merged.append(prefix[p2])
                    p2 += 1

            merged.extend(prefix[p1:mid])
            merged.extend(prefix[p2:right])

            prefix[left:right] = merged

            return count

        return merge_sort(0, len(prefix))