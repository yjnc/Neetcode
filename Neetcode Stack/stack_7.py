class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        stack = [] # (index, height)
        largest = 0
        
        for i, h in enumerate(heights):
            startI = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                largest = max(largest, prevH * (i - prevI))
                startI = prevI
            
            stack.append((startI, h))
            
        # Once we reach end of for loop, we must iterate one last time
        # to calculate the area of remaining rectangles in stack
        for i, h in stack:
            #mult by len(heights), bc the rectangles left can be extended all the way to the end
            largest = max(largest, h * (len(heights) - i))
            
        return largest
    
    
solution = Solution()
heights = [2,1,5,6,2,3] # 10
# heights = [0,0,0,0]
# heights = [2,4] #4
print(solution.largestRectangleArea(heights))