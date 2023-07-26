import math
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        
        while l <= r:
            # must add to l since the index is offset by x amount starting at l
            mid = l + math.floor((r - l) / 2)
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