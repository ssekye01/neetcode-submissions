class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seq = {'(':')',
               '[':']',
               '{':'}'}
        for i in s:
            if i in seq:
                stack.append(i)
            else:
                if not stack or seq[stack[-1]] != i: 
                    return False 
                stack.pop()
        return True if not stack else False
