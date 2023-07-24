from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        # SOLUTION: O(n) time
        # # deque provides O(1) time complexity for append / pop
        # maxNums = []
        # q = deque()
        # l = r = 0
        # while r < len(nums):
        #     # pop values smaller than current number from queue
        #     while q and q[-1] < nums[r]:
        #         q.pop()
        #     q.append(nums[r])
        
        #     # make sure the window is at least equal to k to start updating the max value of each window
        #     if (r + 1) >= k:
        #         maxNums.append(q[0])
        #         if nums[l] == q[0]:
        #             q.popleft()
        #         l += 1
        #     r += 1
            
        # return maxNums
        
        
        
        
        # Alternative Solution using Initial Run
        
        q = deque() # stores index
        maxNums = []
        
        # Initial run
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        maxNums.append(nums[q[0]])
        
        l = 0
        for r in range(k,len(nums)):
            if q[0] == l:
                q.popleft()
            l += 1
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            maxNums.append(nums[q[0]])
            
        return maxNums


solution = Solution()
nums, k = [1,3,-1,-3,5,3,6,7], 3 # [3,3,5,5,6,7]
# nums, k = [1,3,-1,-3,-2,3,6,7], 3 # [3,3,-1,3,6,7]
print(solution.maxSlidingWindow(nums, k))