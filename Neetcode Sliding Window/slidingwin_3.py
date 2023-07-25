from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        '''
        Brute force: check every substring, will be O(n^2) 
        Alt Solution:
        Establish window with l, r pointers
        Increment count of chars for s[r]
        Take window len - most freq char count and check if <= to k
        If so, valid so increment r by one and repeat process
        If invalid, increment l by one and repeat process
        '''
        
        # Using helper function exceeds time limit:
        
        # def mostFreqChar(s: str) -> int:
        #     count = defaultdict(int)
            
        #     for c in s:
        #         count[c] += 1
                
        #     return max(count.values())   
        
        
        # max_len = 0
        # l = 0
        
        # cur = ''
        
        # for r in range(len(s)):
        #     cur += s[r]
        #     changeChars = (r - l + 1) - mostFreqChar(cur) # number of chars to change
        #     if changeChars > k:
        #         l += 1
        #         cur = cur[1:]
        #     else:
        #         max_len = max(max_len, len(cur))
            
        
        # return max_len
        
        
        count = {}
        mode = 0
        l = 0
        
        for r in range(len(s)):
            # Count occurences of each char
            count[s[r]] = 1 + count.get(s[r], 0) # if the char dne in dictionary, "0" ensures we set default value to 0
            # Update to the most freq occurence value
            mode = max(mode, count[s[r]])
            
            # If num chars we need to change is greater than allowed, ie. k
            if (r - l + 1) - mode > k:
                # Decrease the window & the count of that char
                # Note we only need to do this once bc size of window increases/decreases by 1 at a time
                count[s[l]] -= 1
                l += 1
        
        return (r - l + 1) # return final length of valid window (we know its valid bc we check via if statement in loop)
        
        
        
           
        


solution = Solution()
s = "AABABBA" 
k = 1
print(solution.characterReplacement(s,k))