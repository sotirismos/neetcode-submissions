class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sliding_pointer = len(nums1) - 1
        nums1_pointer = m - 1
        nums2_pointer = n - 1
        while nums1_pointer >= 0 and nums2_pointer >= 0:
            if nums1[nums1_pointer] > nums2[nums2_pointer]:
                nums1[sliding_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
            elif nums1[nums1_pointer] < nums2[nums2_pointer]:
                nums1[sliding_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1
            else:
                nums1[sliding_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
            sliding_pointer -= 1
        
        if nums1_pointer >= 0:
            nums1[:sliding_pointer + 1] = nums1[:nums1_pointer + 1]
        
        if nums2_pointer >= 0:
            nums1[:sliding_pointer + 1] = nums2[:nums2_pointer + 1]

            