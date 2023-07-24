import numpy
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # this solution works but not for really long lists
        # res = [0] * len(nums)

        # for i in range(len(nums)):
        #     copy = nums.copy()
        #     del copy[i]
        #     res[i] = numpy.prod(copy)
        
        # return res
        
        # alternative solution if division was allowed in the prompt:
        
        # res = []
        # prods = numpy.prod(nums)
        # for i in range(len(nums)):
        #   res[i] = int(prods // nums[i])
        # return res

        res = []

        for i in range(len(nums)):
            pre = numpy.prod(nums[0:i])
            post = numpy.prod(nums[i + 1:])

            res.append(int(pre*post))
        
        return res
    
solution = Solution()
nums = [2,2,3,4]
print(solution.productExceptSelf(nums))