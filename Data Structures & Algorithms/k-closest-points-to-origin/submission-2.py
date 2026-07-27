class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            point_x = point[0]
            point_y = point[1]
            distance = math.sqrt(point_x ** 2 + point_y ** 2)
            heapq.heappush(max_heap, (-distance, point_x, point_y))
        
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        return [(point_x, point_y) for distance, point_x, point_y in max_heap]