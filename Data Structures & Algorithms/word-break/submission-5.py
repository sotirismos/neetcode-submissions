class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}
        
        return self.dfs(s, wordDict, 0, cache)

    def dfs(self, s: str, wordDict: set[str], index: int, cache: dict) -> bool:
        if index in cache:
            return cache[index]
        
        for j in range(index, len(s)):
            if s[index:j + 1] in wordDict:
                if self.dfs(s, wordDict, j + 1, cache):
                    cache[index] = True
                    return True
        cache[index] = False
        return False