class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs: 
            encoded.append(str(len(string)))
            encoded.append('#')
            encoded.append(string)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        count = 0 
        while count < len(s):
            string = []
            length = 0 
            while s[count] != '#':
                length = (length * 10) + int(s[count])
                count += 1
            count += 1
            for i in range(length):
                string.append(s[count])
                count += 1
            result.append(''.join(string))
        return result
