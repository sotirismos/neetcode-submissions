class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        state = {}
        current_window_length = 0
        max_window_length = 0

        for end in range(len(s)):
            state[s[end]] =  state.get(s[end], 0) + 1
            current_window_length += 1

            while current_window_length - max(state.values()) > k:
                state[s[start]] -= 1
                current_window_length -= 1
                start += 1
                if state[s[start]] == 0:
                    del state[s[start]]
            
            max_window_length = max(max_window_length, current_window_length)

        return max_window_length   