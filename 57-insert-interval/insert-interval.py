class Solution:
    def insert(self, intervals, newInterval):

        ans = []

        for interval in intervals:

            # Before newInterval
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # Overlapping
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            # After newInterval
            else:
                ans.append(newInterval)
                newInterval = interval

        ans.append(newInterval)

        return ans