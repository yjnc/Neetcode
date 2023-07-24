class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        
        '''
        cars can't exceed target integer
        cars with highest starting pos has higher chance of arriving at target first
        so... sort (pos, speed) in decreasing order
        
        distance = target - position
        time = distance / speed
        
        the car will lower time will catch up to ones with greater time
        '''
        
        stack = []
        
        # summarized ver of lines: pair = [(p,s) for p,s in zip(position, speed)], pair.sort(reverse=True)        
        for p, s in sorted(zip(position, speed), reverse=True): 
            distance = target - p
            time = distance / s
            
            if not stack:
                stack.append(time)
            
            elif time > stack[-1]:
                stack.append(time)
                
        return len(stack) 
    
    
solution = Solution()
target, position, speed = 12, [10,8,0,5,3], [2,4,1,1,3] # 3
print(solution.carFleet(target, position, speed))