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
        
        for interval_index in range(len(intervals_sorted) - 1):
            end_time = intervals_sorted[interval_index].end
            start_next = intervals_sorted[interval_index + 1].start
            if end_time > start_next:
                return False
        
        return True