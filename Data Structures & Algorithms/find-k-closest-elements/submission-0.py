class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        l = left - 1
        r = left
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
        
        return arr[l+1:r]