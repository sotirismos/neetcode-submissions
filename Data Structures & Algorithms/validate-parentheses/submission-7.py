class Solution:
    def isValid(self, s: str) -> bool:
        correspondences = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in correspondences.values():
                stack.append(char)
            else:
                if stack and stack[-1] == correspondences[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0