class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        # stack will store index of values in decreasing order
        stack = []
        res = [0] * len(temp)
        
        # initializing the stack to compare
        stack.append(0)
        
        for i in range(1, len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
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