"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_sorted = sorted(intervals, key=lambda x: x.start)

        for index in range(len(intervals) - 1):
            if intervals_sorted[index].end > intervals_sorted[index + 1].start:
                return False
        
        return True