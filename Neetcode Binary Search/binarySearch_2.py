class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        given m x n matrix with two properties: 
            - each row sorted in non-decreasing order
            - first integer of each row greater than last int of prev row
        given target, return true if target is in matri or false otherwise
        O(log(m * n))
        '''
        # Binary search solution
        top, bottom = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        
        # searching for row where target is within range of 0th and -1th intger of that row
        while top <= bottom:
            row = top + ((bottom - top) // 2)
            if matrix[row][r] < target:
                top = row + 1
            elif matrix[row][l] > target:
                bottom = row - 1
            elif matrix[row][l] == target or matrix[row][r] == target:
                return True
                
            else:
                break
            
        # searching for target in row    
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                        
        return False
       
       
        # Brute Force Solution O(m * n)
       
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