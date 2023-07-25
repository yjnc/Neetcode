from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
    
        # rows = defaultdict(set)
        # cols = defaultdict(set)
        # squares = defaultdict(set)
        
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if (board[r][c] in rows[r] or 
        #             board[r][c] in cols[c] or 
        #             board[r][c] in squares[(r//3, c//3)]):
        #             return False
                
        #         rows[r].add(board[r][c])
        #         cols[r].add(board[r][c])
        #         squares[(r//3, c//3)].add(board[r][c])
                
        # return True
    
        # alternative solution:
        
        rows = [set() for _ in range(9)] # the underscore indicates we are uninterested in the "i" for every iteration
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.': 
                    continue
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[i // 3][j // 3]):
                    return False
                
                
                # you can add and remove elements from a set 
                # the elements must be hashable (ie. have one hash value assigned to it and not change)
                rows[i].add(num) 
                cols[j].add(num)
                boxes[i // 3][j // 3].add(num)
                print(boxes)

        return True
            

solution = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))