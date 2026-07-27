class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone_weight for stone_weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            if first > second:
                heapq.heappush(stones, (first - second) * -1)
        
        return stones[0] * -1 if len(stones) > 0 else 0
                