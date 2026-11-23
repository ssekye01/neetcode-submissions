class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        l, r = 0, len(s1) - 1
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:r])
        while r < len(s2):
            s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1
            if s2_dict == s1_dict:
                return True
            s2_dict[s2[l]] -= 1
            l += 1
            r += 1
        return False