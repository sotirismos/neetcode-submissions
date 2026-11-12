class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = []
        for num in arr:
            dist = abs(num - x)
            distances.append((-dist, -num))
        
        heapq.heapify(distances)

        while len(distances) > k:
            heapq.heappop(distances)
        
        output = []
        for _, num in distances:
            output.append(-num)
        
        return sorted(output)