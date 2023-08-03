class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Binary Search solution
        
        # l, r = 0, len(nums) - 1
        
        # while l <= r:
        #     mid = (l + r) // 2
            
        #     if nums[mid] == target:
        #         return mid
            
        #     elif nums[l] <= nums[mid]:
        #         if target > nums[mid] or target < nums[l]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1                
        #     else:
        #         if target < nums[mid] or target > nums[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
                    
        # return -1          
        
        # Alternate Solution
        if target in nums:
            return nums.index(target)
        
        
solution = Solution()
nums, target = [4,5,6,7,0,1,2], 0 #4
nums, target = [4,5,6,7,0,1,2], 3 #-1
nums, target = [0,1,2,4,5,6,7], 3 #-1
print(solution.search(nums, target))