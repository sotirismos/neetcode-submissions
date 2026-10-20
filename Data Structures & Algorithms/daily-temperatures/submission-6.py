class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                starting_day = stack.pop()
                day_diff = index - starting_day
                output[starting_day] = day_diff
            stack.append(index)
        
        return output
