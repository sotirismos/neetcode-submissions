class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        index = 0
        while index < len(temperatures):
            if not stack:
                stack.append(index)
            else:
                if temperatures[index] < temperatures[stack[-1]]:
                    stack.append(index)
                else:
                    while stack and temperatures[index] > temperatures[stack[-1]]:
                        starting_day_index = stack.pop()
                        output[starting_day_index] = index - starting_day_index
                stack.append(index)
            index += 1
        return output
