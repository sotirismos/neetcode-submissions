class Solution:
    def simplifyPath(self, path: str) -> str:
        str_stack = []
        cur = ""
        for char in path + "/":
            if char == '/':
                if cur == "..":
                    if str_stack:
                        str_stack.pop()
                elif cur != "" and cur != ".":
                    str_stack.append(cur)
                cur = ""
            else:
                cur += char

        return "/" + "/".join(str_stack)