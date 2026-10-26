class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output_intervals = []

        # Phase 1: add intervals to the new list until you find an overlapping one
        index = 0
        while index < len(intervals):
            if intervals[index][1] < newInterval[0]:
                output_intervals.append(intervals[index])
                index += 1
            else:
                break

        # Phase 2: absorb overlappers, widening the window each time
        while index < len(intervals):
            if newInterval[1] >= intervals[index][0]:
                newInterval[0] = min(intervals[index][0], newInterval[0])
                newInterval[1] = max(intervals[index][1], newInterval[1])
                index += 1
            else:
                break
        output_intervals.append([newInterval[0], newInterval[1]])
        
        # Phase 3: append what interval is left
        while index < len(intervals): 
            output_intervals.append(intervals[index])  
            index += 1     

        return output_intervals

