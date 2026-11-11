class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            dist = -(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(maxHeap, [dist, point[0], point[1]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        output = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            output.append([x, y])
        
        return output