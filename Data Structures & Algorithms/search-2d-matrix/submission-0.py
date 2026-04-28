class Solution:

    def binarySearch(self, array, target): 
        start = 0 
        end = len(array) - 1
        
        while start <= end: 
            pivot = math.ceil((end - start) // 2) + start

            if array[pivot] == target: 
                return True 

            if array[pivot] < target: 
                start = pivot + 1
            else: 
                end = pivot - 1

        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # binary search over first numbers to identify where? 
        # then binary search again ?

        start = 0 
        end = len(matrix) - 1
        
        while start <= end: 
            pivot = math.ceil((end - start) // 2) + start

            pivot_row = matrix[pivot] 
            print(f"pivot row {pivot_row}")  
            starting = pivot_row[0]
            ending = pivot_row[len(pivot_row) - 1]

            if target == starting or target == ending: 
                return True

            if target > starting and target < ending: 
                print("looking in ")
                return self.binarySearch(pivot_row, target)

            elif target < starting: 
                end = pivot - 1
            else: 
                start = pivot + 1 


        return False