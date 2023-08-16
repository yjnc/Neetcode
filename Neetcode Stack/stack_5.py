class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        '''
        Given temperatures return an array answer such that answer[i] is number of days to wait after ith day to get warmer temp
        if no future day possible, answer[i] = 0
        '''
        # stack will store index of values in decreasing order
        stack = []
        res = [0] * len(temp)
        
        # initializing the stack to compare
        stack.append(0)
        
        for i in range(1, len(temp)):
            # compare temp value at top to cur temp
            while stack and temp[i] > temp[stack[-1]]:
                # add the difference in index bt cur and top value at stack
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return res
                
                
    
    
solution = Solution()
temp = [73,74,75,71,69,72,76,73] #[1,1,4,2,1,1,0,0]
# temp = [30,40,50,60] #[1,1,1,0]
# temp = [0,0,0] #[0,0,0]
# temp = [70,60,50,40,30] #[0,0,0,0,0]
print(solution.dailyTemperatures(temp))