class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time
        intervals = sorted(intervals, key=lambda x: x[0])

        output = []
        index = 0
        # Phase 1
        while index < len(intervals) - 1:
            if intervals[index][1] < intervals[index + 1][0]:
                output.append(intervals[index])
                index += 1
            else:
                intervals[index + 1][0] = min(intervals[index][0], intervals[index + 1][0])
                intervals[index + 1][1] = max(intervals[index][1], intervals[index + 1][1])
                index += 1
        output.append(intervals[index])
        return output
                 