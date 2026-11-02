class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        second_slow = 0
        while second_slow != slow:
            second_slow = nums[second_slow]
            slow = nums[slow]
        
        return second_slow