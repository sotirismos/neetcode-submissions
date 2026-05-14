class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while numbers[right_pointer] + numbers[left_pointer] != target:
            if numbers[right_pointer] + numbers[left_pointer] > target:
                right_pointer -= 1
            else:
                left_pointer += 1
        return [left_pointer + 1, right_pointer + 1]
                