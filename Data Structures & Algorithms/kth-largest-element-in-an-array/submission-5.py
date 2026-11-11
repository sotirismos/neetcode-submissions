class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = nums[0:k]
        heapq.heapify(k_largest)

        for num in nums[k:]:
            if num > k_largest[0]:
                heapq.heappop(k_largest)
                heapq.heappush(k_largest, num)
        
        return k_largest[0]