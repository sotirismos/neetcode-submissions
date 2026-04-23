class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            found = False
            for j in range((i + 1), len(temperatures)):
                count += 1
                if temperatures[i] < temperatures[j]:
                    result.append(count)
                    found = True
                    break
            if not found:
                result.append(0)
        return result