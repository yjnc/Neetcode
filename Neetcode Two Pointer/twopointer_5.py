class Solution:
    def trap(self, height: list[int]) -> int:
        
        # BRUTE FORCE, TIMES OUT FOR LONG LISTS
        # total = 0
        
        # for i in range(0, len(height)):
        #     print("i:", i)
        #     l = 0
        #     for n in height[0:i]:
        #         if n > l:
        #             l = n
        #     print("left:", l)
            
        #     r = 0
        #     for n in height[i:]:
        #         if n > r:
        #             r = n
        #     print("right:", r)
            
        #     amt = min(l, r) - height[i]
        #     print("amt:", amt)
        #     if amt > 0:
        #         total += amt
        
        # print("total:", total)
        # return total
        
        
        total = 0
        
        l, r = 0, len(height) - 1
        l_max, r_max  = height[l], height[r]
        
        while l < r:
            # this takes the minimum height to calc with
            # note: min(l,r) - height[i] = amount water at i
            if l_max < r_max:
                # keep track of left max
                # note by += 1 right away, we ignore the left most height 
                # since there's no bar to contain water to its left
                l += 1 
                l_max = max(l_max, height[l]) 
                total += l_max - height[l]
            
            else:
                # keep track of right max
                # note by += 1 right away, we ignore the right most height 
                # since there's no bar to contain water to its right
                r -= 1
                r_max = max(r_max, height[r])
                total += r_max - height[r]   
        
        return total
        
        
        
        
        
        
    
solution = Solution()
height = [4,2,0,3,2,5]
print(solution.trap(height))

# expected solution: 9