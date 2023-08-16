class Solution:
    def findMin(self, nums: list[int]) -> int:
        '''
        array of length n sorted in ascending order is rotated between 1 and n times
        given nums of unique elements, return min element of this array
        O(log n) 
        '''
        l, r = 0, len(nums) - 1
        minNum = float("inf")
        
        while l <= r:
            mid = (l + r) // 2
            minNum = min(minNum, nums[mid])

            # Means min num is to right of mid
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # Means min num is to the left of mid
            else:
                r = mid - 1
                
        return minNum
    
    
solution = Solution()
# nums = [3,4,5,1,2] # 1
# nums = [4,5,6,7,0,1,2] # 0
nums = [11,13,15,17] # 11
print(solution.findMin(nums))