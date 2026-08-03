class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for index, char in enumerate(s):
            if char == '(':
                left_stack.append(index)
            elif char == '*':
                star_stack.append(index)
            else:
                if not left_stack and not star_stack:
                    return False
                if left_stack:
                    left_stack.pop()
                else:
                    star_stack.pop()
        
        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False
        
        return not left_stack