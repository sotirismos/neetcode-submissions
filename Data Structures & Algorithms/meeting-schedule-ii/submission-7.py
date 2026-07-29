"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda pair: pair.start)
        min_heap = []
        rooms = 0
        for interval in intervals:
            if len(min_heap) < 1:
                heapq.heappush(min_heap, interval.end)
                rooms = max(rooms, len(min_heap))
            else:
                if interval.start < min_heap[0]:
                    heapq.heappush(min_heap, interval.end)
                else:
                    finished_meeting = heapq.heappop(min_heap)
                    heapq.heappush(min_heap, interval.end)
                rooms = max(rooms, len(min_heap))
        return rooms
