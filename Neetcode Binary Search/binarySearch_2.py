import math
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        
        while top <= bottom:
            row = top + math.floor((bottom - top) / 2)
            if matrix[row][r] < target:
                top = row + 1
            elif matrix[row][l] > target:
                bottom = row - 1
            elif matrix[row][l] == target or matrix[row][r] == target:
                return True
                
            else:
                break
            
        while l <= r:
            mid = l + math.floor((r - l) / 2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                        
        return False
       
       
       #Non Binary Search solution (Brute force)
       
    #    row = len(matrix)
    #    col = len(matrix[0])
       
    #    for r in range(row):
    #        for c in range(col):
    #            if matrix[r][c] == target:
    #                return True
       
       
                    
solution = Solution()
matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3 # True
# matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13 # False
print(solution.searchMatrix(matrix, target))