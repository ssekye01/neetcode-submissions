class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 
        max_length = 1 
        l = 0 
        seen = {s[0]: 1}
        for r in range(1, len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1 
            max_length = max(max_length, r - l + 1)
        return max_length