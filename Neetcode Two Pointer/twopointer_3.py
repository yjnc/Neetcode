class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        #NEED TO DEBUG

        # case where nums is less than 3
        if len(nums) < 3:
            return []

        solution = set()

        i = 0
        j = 1

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i + 1]:
                continue


            while j <= len(nums)-2:
                target = -1 * (nums[i] + nums[j])

                if target in nums[j + 1:]:
                    # soln = [nums[i], nums[j], target]
                    # soln.sort()
                    # if soln not in solution:
                    #     solution.append(soln)
                    solution.add(tuple(sorted([nums[i], nums[j], target])))
                
                j += 1

        print(solution)
        return solution
    
solution = Solution()
nums = [3,0,-2,-1,1,2]
print(solution.threeSum(nums))
# expected soln: [[-2,-1,3],[-2,0,2],[-1,0,1]]

            



