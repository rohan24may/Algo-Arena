class Solution:
    def insert(self, intervals, newInterval):

        ans = []

        for interval in intervals:

            # 1. Before
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # 2. Overlap
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            # 3. After
            else:
                ans.append(interval)

        ans.append(newInterval)

        ans.sort(key=lambda x: x[0])

        return ans