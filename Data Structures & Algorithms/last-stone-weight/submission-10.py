class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            heaviest = heapq.heappop(neg_stones) * -1
            if heaviest > neg_stones[0] * -1:
                second_heaviest = heapq.heappop(neg_stones) * -1
                heapq.heappush(neg_stones, (heaviest - second_heaviest) * -1)
            else:
                heapq.heappop(neg_stones) * -1
        
        if len(neg_stones):
            return neg_stones[0] * -1
        else:
            return 0