class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for word in strs:
            char_count = [0] * 26
            for char in word:
                unicode = ord(char) - ord('a')
                char_count[unicode] += 1
            if tuple(char_count) in anagrams:
                anagrams[tuple(char_count)].append(word)
            else:
                anagrams[tuple(char_count)] = [word]
        out = []
        for anagram in anagrams.values():
            out.append(anagram)
        
        return out