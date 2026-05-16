class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        output = [0 for _ in range(0, len(nums))]
        for i, val in enumerate(nums):
            pos = (i + k) % len(nums)
            output[pos] = val
        nums[:] = output[:]


        