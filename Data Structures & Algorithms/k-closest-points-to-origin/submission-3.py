class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            dist = (point[0] ** 2) + (point[1] ** 2)
            distances.append((-dist, point[0], point[1]))
        # construct a max_heap and start popping elements until the length of the heap is K (meaning the K closest to origin)
        heapq.heapify(distances)

        for _ in range(len(distances) - k):
            heapq.heappop(distances)

        output = []
        for dist, x, y in distances:
            output.append([x, y])
        
        return output