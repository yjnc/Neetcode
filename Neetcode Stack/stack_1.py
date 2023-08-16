class Solution:
    def isValid(self, s: str) -> bool:
        '''
        given string s containing characters '(', ')', '{', '}', '[', ']'
        determine if string is valid:
            - open brackets must be closed by same type
            - open brackets must be closed in correct order
            - every close bracket has corresponding open bracket of same type
        '''
        # dict corresponding valid close brackets to valid open brackets
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            # Open brackets:
            # add open brackets to stack
            if char not in brackets:
                stack.append(char)
                continue
            
            # Close brackets:
            # if no open bracket in stack or open bracket in stack doesn't match the close bracket
            if not stack or stack[-1] != brackets[char]:
                return False
            
            # remove the open bracket from stack once close bracket found
            stack.pop()
            
        return not stack 
    
    
    
    
solution = Solution()
s = "()" # True
# s = "()[]{}" # True
# s = "(]" # False
print(solution.isValid(s))