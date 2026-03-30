# import numpy as np
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         print(board)
#         length = len(board)
#         board = np.array(board) 

#         # check cols 
#         for index in range(length):
#             element_row, count_row = np.unique(board[index], return_counts=True) 
#             element_col, count_col = np.unique(board[:,index], return_counts=True)
#             to_check_row = count_row[1:] if element_row[0] == '.' else count_row
#             to_check_col = count_col[1:] if element_col[0] == '.' else count_col
#             if np.any(to_check_row != 1) or np.any(to_check_col != 1): 
#                 return False

#         squares = board.reshape(3, 3, 3, 3).transpose(0, 2, 1, 3).reshape(9, 3, 3)
#         for square in squares: 
#             square_flattened = square.flatten() 
#             unq, count = np.unique(square_flattened, return_counts=True)
#             to_check = count[1:] if unq[0] == '.' else count
#             if not np.all(to_check == 1):
#                 return False
       
#         return True

from collections import defaultdict
import numpy as np
import math 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        print(np.array(board))

        count_rows = [{} for i in range(9)]
        count_cols = [{} for i in range(9)]
        count_boxes = [{} for i in range(9)]

        for row_number, row in enumerate(board): 
            for col_number, element in enumerate(row): 
                if element != '.':
                    element = int(element)
                    count_rows[row_number][element] = count_rows[row_number].get(element,0) + 1
                    count_cols[col_number][element] = count_cols[col_number].get(element,0) + 1
                    box_index = (row_number // 3) * 3 + (col_number // 3)
                    count_boxes[box_index][element] = count_boxes[box_index].get(element,0) + 1


        for i in range(9): 
            row = count_rows[i]
            col = count_cols[i]
            box = count_boxes[i]

            row_check = all(elem == 1 for elem in row.values())
            col_check = all(elem == 1 for elem in col.values())
            box_check = all(elem == 1 for elem in box.values())

            if not row_check or not col_check or not box_check: 
                return False



        






            

        return True
