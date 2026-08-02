class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for index, char in enumerate(s):
            last_index[char] = index

        output = []
        size = 1
        partition_end = float('-inf')
        for index, char in enumerate(s):
            partition_end = max(partition_end, last_index[char])
            if index == partition_end:
                output.append(size)
                size = 1
            else:  
                size += 1 

        return output
