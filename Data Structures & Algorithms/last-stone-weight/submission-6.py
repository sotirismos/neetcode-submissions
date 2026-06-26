class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            elif stones[0] < stones[1]:
                stones[1] = stones[1] - stones[0]
                stones.pop(0)
            else:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
        if stones:
            return stones[0] 
        else:
            return 0