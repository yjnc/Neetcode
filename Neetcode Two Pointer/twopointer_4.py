class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        # BRUTE FORCE ANSWER:
        # Answer works but exceeds time limit:
        # maxWater = 0
        # l, r = 0, len(height) - 1

        # while l != len(height) - 1:
        #     if l == r:
        #         l += 1
        #         r = len(height) - 1
        #     else:
        #         amtWater = abs(l - r) * min(height[l], height[r])
        #         maxWater = max(maxWater, amtWater)
        #         r -= 1
        # return maxWater
        
        
        # LINEAR SOLUTION
        maxWater = 0
        l, r = 0 , len(height) - 1
        
        while l < r:
            curWater = (r - l) * min(height[l], height[r])
            maxWater = max(maxWater, curWater)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
            

solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height)) #expected soln: 49