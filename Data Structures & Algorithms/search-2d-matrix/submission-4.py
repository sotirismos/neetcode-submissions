class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return self.binary_search(matrix[mid], target)
        return False
        
    
    def binary_search(self, arr: list, target: int):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if  target > arr[mid]:
                left = mid + 1
            elif target < arr[mid]:
                right = mid - 1
            else:
                return True
        return False
