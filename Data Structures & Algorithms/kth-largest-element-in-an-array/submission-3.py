class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapq.heapify(nums)
        for count in range(k - 1):
            heapq.heappop(nums)
        return nums[0] * -1