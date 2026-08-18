class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        substrings = []
        self.explore(0, s, partitions, substrings)
        return partitions

    def ispali(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    

    def explore(self, index: int, s: str, partitions: List[List[str]], substrings: List[str]):
        if index >= len(s):
            partitions.append(substrings.copy())
            return
        
        for end in range(index, len(s)):
            if self.ispali(s, index, end):
                substrings.append(s[index:end + 1])
                self.explore(end + 1, s, partitions, substrings)
                substrings.pop()


        
