class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        index = 0
        new_interval_start = newInterval[0]
        new_interval_end = newInterval[1]
        # Phase 1
        while index < len(intervals):
            if intervals[index][1] < new_interval_start:
                output.append(intervals[index])
                index += 1
            else:
                break
        # Phase 2
        while index < len(intervals):
            if intervals[index][0] <= new_interval_end:
                new_interval_start = min(new_interval_start, intervals[index][0])
                new_interval_end = max(new_interval_end, intervals[index][1])
                index += 1
            else:
                break
        output.append([new_interval_start, new_interval_end])
        # Phase 3
        while index < len(intervals):
            output.append(intervals[index])
            index += 1

        return output            
