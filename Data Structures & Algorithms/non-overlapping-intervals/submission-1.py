class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start < last_end:
                output[-1][1] = min(last_end, end)
            else:
                output.append([start, end])
        return len(intervals) - len(output) 
                 