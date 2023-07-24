from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # SOLUTION O(26n) time
        # def alphaCounter(s: str):
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
        #     return count
        
        
        # target = alphaCounter(s1) # target count of each alphabet
        
        # l, r = 0, (len(s1) - 1)
        # while r  < len(s2):
        #     count = alphaCounter(s2[l:r + 1])
        #     if count == target:
        #        return True
        #     else:
        #         l += 1
        #         r += 1
        
        # return False
        
        # # SOLUTION O(n) time using array
        
        # if len(s1) > len(s2):
        #     return False
        
        # s1Count, s2Count = [0] * 26, [0] * 26
        
        
        # # First iteration to find the initial number of matches
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord("a")] += 1
        #     s2Count[ord(s2[i]) - ord("a")] += 1
        # matches = 0
        # for i in range(26):
        #     matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        
        # l = 0
        # # iterate through rest of the string excluding initial window
        # for r in range(len(s1), len(s2)): 
        #     if matches == 26: 
        #         return True
            
        #     # Sliding down the window
        #     # Right window: add new chars
        #     index = ord(s2[r]) - ord('a')
        #     s2Count[index] += 1
        #     if s1Count[index] == s2Count[index]:
        #         # new char match required no of it
        #         matches += 1
        #     elif s1Count[index] + 1 == s2Count[index]:
        #         # one too many of new char so we decrement no of matches
        #         matches -= 1
                
            
        #     # Left window: remove leftmost chars
        #     index = ord(s2[l]) - ord('a')
        #     s2Count[index] -= 1
        #     if s1Count[index] == s2Count[index]:
        #         # new char match required no of it
        #         matches += 1
        #     elif s1Count[index] - 1 == s2Count[index]:
        #         # one too many of new char so we decrement no of matches
        #         matches -= 1
        #     l += 1
        
        # # Need to check one last time bc it doesn't check after the final loop runs
        # return matches == 26


        # SOLUTION O(n) time using Hash maps
        
        if len(s1) > len(s2):
            return False
        
        # Initialize target letters
        target = defaultdict(int)
        for i in range(len(s1)):
            target[s1[i]] += 1
        print("target:", target)
        
        # Sort of like n=0 or n=1 in inductive proofs
        # Check if first window contains the right letters
        have = defaultdict(int)
        for i in range(len(s1)):
            if s2[i] in target:
                have[s2[i]] += 1
        print("have:", have)
                
        l = 0
        # Need to use "if" and not "elif" because it needs to evaluate
        for r in range(len(s1), len(s2)):
            if target == have:
                return True
            # Sliding window down
            # Add new letter to right, increment if matches
            if s2[r] in target:
                have[s2[r]] += 1

            # Remove leftmost letter, decrement if we had it prev
            if s2[l] in target:
                have[s2[l]] -= 1

            l += 1
        
        return target == have
           
solution = Solution()
# s1, s2 = "hello", "ooolleoooleh" # False
# s1, s2 = "ab", "eidbaooo" # True
s1, s2 = "ab", "eidboaoo" # False
print(solution.checkInclusion(s1, s2))