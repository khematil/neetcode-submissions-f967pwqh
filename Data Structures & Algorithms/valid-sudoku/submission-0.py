from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ((board[r][c] in rows[r]) or # if the value of board[r][c] occurred in the current row then its a dupe
                    (board[r][c] in cols[c]) or # if the value of board[r][c] occurred in the current col then its a dupe
                    (board[r][c] in squares[r//3, c//3])): # if the value  of board[r][c] occurred in the current square then its a dupe
                    return False
                
                # update hashset
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
    
        return True