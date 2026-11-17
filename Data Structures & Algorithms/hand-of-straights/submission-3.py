class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = {}
        for num in hand:
            counter[num] = counter.get(num, 0) + 1

        unique_elements = list(set(hand))
        heapq.heapify(unique_elements)

        while unique_elements:
            current_smallest = unique_elements[0]
            for next_element in range(current_smallest, current_smallest + groupSize):
                if (next_element not in counter) or (counter[next_element] == 0):
                    return False
                else:
                    counter[next_element] -= 1
                    if counter[next_element] == 0:
                        if next_element != unique_elements[0]:
                            return False
                        else:
                            heapq.heappop(unique_elements)
        
        return True