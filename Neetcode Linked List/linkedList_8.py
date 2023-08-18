class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        '''
        Given nums containing n + 1 integers where each int is in the range [1,n]
        only one repeated number in nums, return the repeated number 
        
        rules: without modifying nums and use only constant extra space
        (ie. memory you take to solve the problem doesn't depend on the input variable)
        '''
        
        '''
        Math Proof: first note that the first node of cycle is where there are two pointers, thus creating a cycle
        hence, we must find this node where the cycle first starts.
        
        p: distance from start to first node of cycle 
        c: length of cycle
        x: distance from where slow, fast pointers intersect to the start node of the cycle
        n: integer
        
        2 slow = fast
        2(p + c - x) = p + nc - x
        p - nc = x
        
        because nc is just cycles, we end up at the same node after n cycles,
        thus we can disregard it and we end up with
        p = x
        
        ie. distance from start to first node of cycle is equal to distance from the intersection point
        '''
        # Use index as equivalent to node.next of linked list
        slow, fast = 0, 0
        
        # Find the intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
           
        # Find the start of the cycle 
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
            
solution = Solution()
nums = [1,3,4,2,2] # 2
nums = [3,1,3,4,2] # 3
print(solution.findDuplicate(nums))