class Solution:
 def minMeetingRooms(self, start, end):

    start.sort()
    end.sort()

    i = j = 0
    rooms = 0
    max_rooms = 0

    while i < len(start): # pyright: ignore[reportUndefinedVariable]

        if start[i] < end[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1

        else:
            rooms -= 1
            j += 1

    return max_rooms