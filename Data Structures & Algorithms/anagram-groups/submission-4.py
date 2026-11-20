class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        result = []
        for string in strs:
            sorte = ''.join(sorted(string))
            if sorte not in grouped:
                grouped[sorte] = []
            grouped[sorte].append(string)
        for key,value in grouped.items():
            result.append(value)
        return result