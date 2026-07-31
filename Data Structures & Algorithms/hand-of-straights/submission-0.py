class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_hash_map = {}
        for num in hand:
            if num in hand_hash_map:
                hand_hash_map[num] += 1
            else:
                hand_hash_map[num] = 1
        
        hand.sort()
        for num in hand:
            if hand_hash_map[num] > 0:
                for member in range(num, num + groupSize):
                    if member in hand_hash_map:
                        hand_hash_map[member] -= 1
                    else:
                        return False
        
        return True