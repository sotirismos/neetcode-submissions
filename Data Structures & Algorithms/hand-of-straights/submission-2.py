class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_hash_map = {}
        for num in hand:
            if num in hand_hash_map:
                hand_hash_map[num] += 1
            else:
                hand_hash_map[num] = 1
        
        min_heap = [key for key in hand_hash_map.keys()]
        heapq.heapify(min_heap)
        while min_heap:
            start = min_heap[0] 
            for member in range(start, start + groupSize):
                if member in hand_hash_map:
                    hand_hash_map[member] -= 1
                else:
                    return False
                
                if hand_hash_map[member] == 0:
                    if member != min_heap[0] :
                        return False
                    heapq.heappop(min_heap)
    
        return True