class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for string in strs:
            ord_list = [0] * 26
            for char in string:
                ord_list[ord(char) - ord('a')] += 1
            
            ord_tuple = tuple(ord_list)
            if ord_tuple in anagrams_dict:
                anagrams_dict[ord_tuple].append(string)
            else:
                anagrams_dict[ord_tuple] = [string]
        
        anagram_list = []
        for key, value in anagrams_dict.items():
            anagram_list.append(value)
        
        return anagram_list
