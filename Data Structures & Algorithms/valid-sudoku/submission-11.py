class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            #check row 
            row_values = set()
            column_values = set()
            for x in range(0,9):
                if board[i][x] in row_values:
                    return False
                    
                elif board[i][x] != ".":
                    row_values.add(board[i][x])
                
                if board[x][i] in column_values:
                    return False
                elif board[x][i] != ".":
                    column_values.add(board[x][i])

        for i in range(1,9,3):
            for x in range(1,9,3):
                small_box = set()
                for y in range(-1,2):
                    for z in range(-1,2):
                        
                        if board[i+y][x+z] in small_box:
                            return False
                        
                        elif board[i+y][x+z] != ".":
                            small_box.add(board[i+y][x+z])
        return True