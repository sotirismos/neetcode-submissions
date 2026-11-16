class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        # Add element to small heap
        heapq.heappush(self.small_heap, num * -1)

        # Check if largest element in small heap is smaller than the smallest in large heap
        if self.small_heap and self.large_heap:
            if self.small_heap[0] * -1 > self.large_heap[0]:
                element = heapq.heappop(self.small_heap) * -1
                heapq.heappush(self.large_heap, element)
        
        # Handle uneven siz
        if len(self.small_heap) > len(self.large_heap) + 1:
            element = heapq.heappop(self.small_heap) * -1
            heapq.heappush(self.large_heap, element)
        
        if len(self.large_heap) > len(self.small_heap) + 1:
            element = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, element * -1)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return self.small_heap[0] * -1
        elif len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0] 
        else:
            return (self.small_heap[0] * -1 + self.large_heap[0]) / 2
        
        