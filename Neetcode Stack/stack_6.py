class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        '''
        n cars going to same destination target miles away (cars can't exceed target integer)
        given arrays position and speed, both of length n, return numnber of car fleets that will arrive at destination
        
        Car Fleet - some non-empty set of cars driving at same position and speed (single car is also a car fleet)
        
        Logic:
        cars with highest starting pos has higher chance of arriving at target first
        so... sort (pos, speed) in decreasing order
        distance = target - position
        time = distance / speed
        the car will lower time will catch up to ones with greater time
        '''
        
        stack = []

        # sorted in decreasing order of positions   
        for p, s in sorted(zip(position, speed), reverse=True): 
            distance = target - p
            time = distance / s
            
            # append times it take for cars to get to destination
            if not stack:
                stack.append(time)
            
            elif time > stack[-1]:
                stack.append(time)
            print(stack)
        return len(stack) 
    
    
solution = Solution()
target, position, speed = 12, [10,8,0,5,3], [2,4,1,1,3] # 3
print(solution.carFleet(target, position, speed))