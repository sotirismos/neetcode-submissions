class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []


        index = 0
        while index < len(intervals) - 1:
            start_time = intervals[index][0]
            end_time = intervals[index][1]

            while index < len(intervals) - 1 and end_time >= intervals[index + 1][0]:
                end_time = max(end_time, intervals[index + 1][1])
                index += 1
            
            merged_intervals.append([start_time, end_time])
            
            index += 1
        
        if not merged_intervals or merged_intervals[-1][1] < intervals[-1][0]:
            merged_intervals.append(intervals[-1])

        return merged_intervals
            
