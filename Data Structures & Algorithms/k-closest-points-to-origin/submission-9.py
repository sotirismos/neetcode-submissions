class Solution:
    def euclidean(self, point) -> int:
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def quickSelect(left, right):
            pivot_index = right
            pivot_distance = self.euclidean(points[pivot_index])

            current_index = left
            for index in range(left, right):
                current_distance = self.euclidean(points[index])
                if current_distance <= pivot_distance:
                    points[current_index], points[index] = points[index], points[current_index]
                    current_index += 1
            
            points[current_index], points[right] = points[right], points[current_index]
                
            if current_index < k - 1:
                return quickSelect(current_index + 1, right)
            elif current_index > k - 1:
                return quickSelect(left, current_index - 1)
            else:
                return points[:k]
            
        return quickSelect(0, len(points) - 1)