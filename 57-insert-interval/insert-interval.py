class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        i = 0
        n = len(intervals)

        # 1. Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 3. Add merged newInterval
        ans.append(newInterval)

        # 4. Add remaining intervals
        ans.extend(intervals[i:])

        return ans