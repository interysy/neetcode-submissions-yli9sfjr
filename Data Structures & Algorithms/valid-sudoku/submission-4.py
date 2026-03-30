import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        board = np.array(board) 

        
        # check cols 
        for index in range(length):
            element_row, count_row = np.unique(board[index], return_counts=True) 
            element_col, count_col = np.unique(board[:,index], return_counts=True)
            to_check_row = count_row[1:] if element_row[0] == '.' else count_row
            to_check_col = count_col[1:] if element_col[0] == '.' else count_col
            # print(f"row {element_row} count {count_row}, to check {to_check_row}")
            # print(f"col {element_col} count {count_col}, to check {to_check_col}")
            # print(np.any(to_check_col != 1))
            if np.any(to_check_row != 1) or np.any(to_check_col != 1): 
                return False
        # print("passed")

        squares = board.reshape(3, 3, 3, 3).transpose(0, 2, 1, 3).reshape(9, 3, 3)
        for square in squares: 
            square_flattened = square.flatten() 
            unq, count = np.unique(square_flattened, return_counts=True)
            to_check = count[1:] if unq[0] == '.' else count
            if not np.all(to_check == 1):
                return False
       


        return True

