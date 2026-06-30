class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded += str(length) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        start_index = 0
        index = 0
        while index < (len(s)):
            if s[index] == "#":
                length = int(s[start_index:index])
                decoded.append(s[index+1:index+1+length])
                start_index = index+1+length
                index  = index+1+length
            else:
                index += 1
        return decoded