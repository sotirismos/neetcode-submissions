class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for index, string in enumerate(strs):
            string_length = len(string)
            encoded_str += str(string_length) + "#" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        output = []
        index = 0
        while index < len(s):
            string_length = ""
            while s[index] != "#":
                string_length += s[index]
                index += 1
            string_length = int(string_length)
            word = ""
            start = index + 1
            end = index + 1 + string_length
            for word_index in range(start, end):
                word += s[word_index]
            output.append(word)
            index += string_length + 1
        return output
