# alternative quicker solution using counter (creates dictionary format tuple)
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # creates a tuple in dict format
        # gives back k number of modes [(num, freq), (num2, freq), ..., (numk, freq)]
        frequent_elements = Counter(nums).most_common(k)

        # takes the "key" from the generated tuple to return the k most freq values
        return [frequent_elements[i][0] for i in range(k)]

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
    

# # my solution
# from collections import defaultdict
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = defaultdict(int)

#         for num in nums:
#             count[num] += 1
        
#         # using lambda function to sort dictionary by the values
#         # return a tuple in format of a dictionary
#         count_sorted = sorted(count.items(), key=lambda x:x[1])

#         freq = []
#         for i in range(1, k+1):
#             freq.append(count_sorted[-i][0])

#         return freq