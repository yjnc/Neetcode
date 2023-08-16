import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        '''
        n piles of bananas, ith pile has piles[i] bananas, has h hours to eat with speed of k
        choose some pile of bananas and eat k from that pile, if less than k bananas, eat all of them and not eat anymore that hour
        return minimum integer k such that all bananas can be eaten within h hours
        '''
        l,r = 1, max(piles)
        speed = max(piles)
        
        while l <= r:
            # Banana eating speed
            k = (l + r) // 2
            
            # Calculating total time needed to eat at speed k
            time = 0
            for b in piles:
                time += math.ceil(b / k)
            
            # Adjusting speed to minimize k
            if time <= h:
                speed = min(speed, k)
                r = k - 1
            else:
                l = k + 1
        
        return speed
    
    
solution = Solution()
piles, h = [3,6,7,11], 8 # 4
# piles, h = [30,11,23,4,20], 5 # 30
print(solution.minEatingSpeed(piles, h))