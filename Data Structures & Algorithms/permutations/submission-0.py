class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for number in nums:
            next_perms = []
            for perm in perms:
                for index in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(index, number)
                    next_perms.append(perm_copy)
            perms = next_perms

        return perms