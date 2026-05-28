class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = {}
        for string in strs:
            count = [0] * 26
            for index, char in enumerate(string):
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key in anagram_dict:
                anagram_dict[key].append(string)
            else:
                anagram_dict[key] = [string]
        output = []
        for key, values in anagram_dict.items():
            output.append(values)
        return output
                