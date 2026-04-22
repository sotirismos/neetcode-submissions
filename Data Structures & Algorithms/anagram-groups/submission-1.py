class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # anagrams = []

        # anagram_dict = {}
        # for word in strs:
        #     sorted_string = "".join(sorted(word))
        #     if sorted_string in anagram_dict:
        #         anagram_dict[sorted_string].append(word)
        #     else:
        #         anagram_dict[sorted_string] = [word]

        # for sorted_string in anagram_dict:
        #     anagrams.append(anagram_dict[sorted_string])

        # return anagrams

        anagram_dict = {}
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord("a")] += 1
            if tuple(char_count) in anagram_dict:
                anagram_dict[tuple(char_count)].append(word)
            else:
                anagram_dict[tuple(char_count)] = [word]
        
        return list(anagram_dict.values())




                