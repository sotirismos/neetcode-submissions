class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        non_overlapping_intervals = []

        for index, interval in enumerate(intervals):
            if not non_overlapping_intervals or non_overlapping_intervals[-1][1] <= interval[0]:
                non_overlapping_intervals.append(interval)

        return len(intervals) - len(non_overlapping_intervals)
