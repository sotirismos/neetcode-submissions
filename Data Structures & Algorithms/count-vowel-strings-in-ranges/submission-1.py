class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = []
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        running_sum = 0
        for word in words:
            if word[0] in vowels_set and word[-1] in vowels_set:
                running_sum += 1
            prefix_sum.append(running_sum)
        
        # [1, 1, 2, 3, 4]

        output = []
        for query in queries:
            end = query[1]
            start = query[0]
            if start == 0:
                output.append(prefix_sum[end])
            else:
                output.append(prefix_sum[end] - prefix_sum[start - 1])
        
        return output