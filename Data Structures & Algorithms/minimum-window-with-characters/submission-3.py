class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(set(t))
        have = 0 
        i = 0
        freq, standard = {}, Counter(t)
        best = [i, float('inf')]
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            length = j - i + 1
            if freq[s[j]] == standard[s[j]]:
                have += 1
            while have == need:
                if length < best[1]:
                    best = [i, length]
                freq[s[i]] -= 1
                if freq[s[i]] < standard[s[i]]:
                    have -= 1
                i += 1
                length -= 1
        if best[1] == float('inf'):
            return ""
        return s[best[0]:(best[0] + best[1])]