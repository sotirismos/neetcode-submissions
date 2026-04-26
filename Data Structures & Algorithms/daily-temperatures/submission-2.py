class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        monotonic_stack = [] # pair: [temp, index]

        for index, temp in enumerate(temperatures):
            count = 0
            while monotonic_stack and temp > monotonic_stack[-1][0]:
                stack_temp, stack_index = monotonic_stack.pop()
                result[stack_index] = (index - stack_index)    
            monotonic_stack.append([temp, index])

        return result
            