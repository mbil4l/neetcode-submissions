class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        uniqElems = set()
        nonEmpty = 0
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    nonEmpty += 1
                    # (r, e) (e, c) (r//3, c//3, e)
                    uniqElems.add((r, board[r][c])) 
                    uniqElems.add((board[r][c], c)) 
                    uniqElems.add((r//3, c//3, board[r][c]))
        return len(uniqElems) == nonEmpty*3


