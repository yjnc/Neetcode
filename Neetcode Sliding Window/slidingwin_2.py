class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        Sliding window: needs two pointers, left & right
        Start iterating down until we hit a duplicate,
        Remove until duplicate is removed
        Then continue sliding down the string
        Keep track of the longest length
        '''
        
        
        chars = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # If duplicates:
            while s[r] in chars: 
                chars.remove(s[l]) # Remove leftmost char in string from set
                l += 1 # Increment the left pointer by one, ie. slide down
                
            chars.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
    
    
    
    
        # ALTERNATE SOLUTION
        max_len = 0
        cur_str = ''
        
        for c in s:
            if c not in cur_str:
                cur_str += c
                max_len = max(len(cur_str), max_len)
            else:
                cur_str = cur_str[cur_str.find(c) + 1:] + c # Take the substring without the duplicate character from the left
        
        return max_len
    

solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))