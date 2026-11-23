class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {s[0] : 1}
        max_f = 1
        max_length = 1
        l = 0
        for idx in range(1, len(s)):
            freq[s[idx]] = freq.get(s[idx], 0) + 1 
            if freq[s[idx]] > max_f: 
                max_f = freq[s[idx]]
            length = idx - l + 1
            while length - max_f > k: 
                freq[s[l]] -= 1
                l += 1
                length -= 1
            max_length = max(max_length, idx - l + 1)
        return max_length