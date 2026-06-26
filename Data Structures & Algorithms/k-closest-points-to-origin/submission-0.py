class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            dist.append(math.sqrt((point[0]**2) + point[1]**2))
        
        sorted_points = [point for dist, point in sorted(zip(dist, points))]
        return sorted_points[:k]