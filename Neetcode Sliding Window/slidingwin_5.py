class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge case
        if t == "":
            return ""

        # Initialize count for string t
        target, count = {}, {}
        for c in t:
            target[c] = 1 + target.get(c, 0)

        
        have, need = 0, len(target)
        window, minLen = [-1, -1], float('inf')
        l = 0
        
        # Iterating over string s with window
        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c, 0)
            
            # Update matching char count
            if c in target and count[c] == target[c]:
                have += 1
            
            
            # While the window contains chars of t...
            while have == need:
                # Update the results
                if (r - l + 1) < minLen:
                    window = [l, r]
                    minLen = (r - l + 1)
                                
                
                # Shift the window, ie. remove leftmost char
                count[s[l]] -= 1
                if s[l] in target and count[s[l]] < target[s[l]]:
                    have -= 1
                l += 1

        
        l, r = window
        return s[l : r + 1] if minLen != float('inf') else ''
                    
                    
                    
                    
                    
                    
                            

solution = Solution()
# s, t = "ADOBECODEBANC", "ABC" # "BANC"
# s, t = "a", "a" # "a"
s, t = "a", "aa" # ""
print(solution.minWindow(s,t))