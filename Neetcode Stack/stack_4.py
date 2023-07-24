class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        #Solution using stack
        
        stack = []
        valid = []
        
        def dfs(openN: int, closeN: int):
            if openN == closeN == n:
                valid.append("".join(stack))
                return
                
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closeN)
                stack.pop()
                
            if closeN < openN:
                stack.append(")")
                dfs(openN, closeN + 1)
                stack.pop()
                
        dfs(0, 0)
        return valid
    
    
    
        # Solution using only dfs
        valid = []
        def dfs(openN, closeN, s):
            if len(s) == n * 2:
                valid.append(s)
                return
            
            if openN < n:
                # we don't need to remove the added parenthesis bc, it's only added upon running recursion
                # so once we exit the recursion (bc it didn't work), then the s go back to its prev version. 
                # ie. if "(()))" didn't work, we exit the recursion and s would be the prev string, "(())"
                dfs(openN + 1, closeN, s + "(")

            if closeN < openN:
                dfs(openN, closeN + 1, s + ")")
        
        dfs(0, 0, '')
        return valid
    
    
    
    
        
solution = Solution()
n = 3 # ["((()))","(()())","(())()","()(())","()()()"]
print(solution.generateParenthesis(n))