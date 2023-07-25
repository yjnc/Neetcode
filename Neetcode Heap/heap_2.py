import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, y-x)
            
        if len(stones) == 1:
            return -stones[0]
        return 0
                
    
solution = Solution()
stones = [2,7,4,1,8,1]
print(solution.lastStoneWeight(stones))
        
        

