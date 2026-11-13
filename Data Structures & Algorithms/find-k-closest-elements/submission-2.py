class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            dist = abs(num - x)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, num))
            else:
                if dist < - max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-dist, num))
        
        out = []
        while max_heap:
            dist, num = heapq.heappop(max_heap)
            out.append(num)
        out.sort() 
        return out
