class Solution:
    def isValid(self, s: str) -> bool:
        correspondences = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in correspondences.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == correspondences[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0