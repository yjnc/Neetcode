import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        two sorted arrays, nums1 & nums2 of size m and n respectively
        return median of two sorted array in O(log(M + n))
        '''
        
        # # O(m + n) solution
        # return statistics.median(sorted(nums1 + nums2))
        
        
        # O(log(m + n)) solution -> note, log solutions are typically binary search solutions
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 # median partition
        
        # Make A the smaller array
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            parA = (l + r) // 2  # mid point of A
            parB = half - parA - 2 # remaning nums to reach half partition
            
            # Ensure the indicies are in bound
            Aleft = A[parA] if parA >= 0 else float('-inf')
            Aright = A[parA + 1] if (parA + 1) < len(A) else float('inf')
            Bleft = B[parB] if parB >= 0 else float('-inf')
            Bright = B[parB + 1] if (parB + 1) < len(B) else float('inf')
        
            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd length case
                if total % 2:
                    return min(Aright, Bright)
                
                # even length case
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # find average value of the ints for median
            
            # Partition not correct
            elif Aleft > Bright:
                r = parA - 1
            else:
                l = parA + 1
        
        
        
        
solution = Solution()
nums1, nums2 = [1,3], [2] # 2
nums1, nums2 = [1,2], [3,4] # 2.5
print(solution.findMedianSortedArrays(nums1, nums2))