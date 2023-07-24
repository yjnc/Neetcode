class Solution:
    def encode(self, strs):
        encoded = ""
        
        for s in strs:
            encoded += str(len(s)) + "{" + s
        
        return encoded
        
    def decode(self, str):
        decoded, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != "{":
                j += 1
            
            length = int(str[i:j])
            decoded.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
            
        return decoded
    
    
solution = Solution()
strs = ["neet", "code"]
encoded = solution.encode(strs)
print("Encoded:", encoded)
print("Decoded:", solution.decode(encoded))
        