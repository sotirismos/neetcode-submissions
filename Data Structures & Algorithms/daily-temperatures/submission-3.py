class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            while stack:
                if temperatures[i] > stack[-1][0]:
                    temp, index = stack.pop()
                    diff = i - index
                    ans[index] = diff
                else:
                    break
            stack.append((temperatures[i], i))
            i += 1
        return ans
