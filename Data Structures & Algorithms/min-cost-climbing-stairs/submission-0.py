class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        path = [0, 0]
        i = 2
        while i <= len(cost) - 1:
            path_cost = min(path[i - 1] + cost[i - 1], path[i -2] + cost[i - 2])
            path.append(path_cost)
            i += 1

        return min(path[-1] + cost[-1], path[-2] + cost[-2])