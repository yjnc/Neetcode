import math
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        Given nums sorted in ascending order and target, search target in nums.
        If target exists, return its index, else -1
        O(log n)
        '''
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # used instead of (l + r) // 2 when len of array exceeds beyond 2^30
            # typically a better choice to not have bugs
            mid = l + ((r - l) // 2) 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    
    
    
solution = Solution()
nums, target = [-1,0,3,5,9,12], 9 #4
nums, target = [-1,0,3,5,9,12], 2 #-1
print(solution.search(nums, target))