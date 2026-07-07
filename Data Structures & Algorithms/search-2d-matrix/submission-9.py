class Solution:


    def binarySearch(self, row : List[int], low : int, high : int, target: int) -> bool: 
        if low > high: 
            return False

        mid = low + ((high-low) // 2)

        if row[mid] == target: 
            return True 

        if row[mid] > target: 
            return self.binarySearch(row, low, mid - 1, target)

        if row[mid] < target: 
            return self.binarySearch(row, mid+1, high, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0 
        high = len(matrix) - 1

        while low <= high: 
            mid = low + ((high-low) // 2)

            if target == matrix[mid][0] or target == matrix[mid][len(matrix[mid]) - 1]:
                return True
    
            if target > matrix[mid][0] and target < matrix[mid][len(matrix[mid])-1]:
                return self.binarySearch(matrix[mid], 0, len(matrix[mid]) - 1, target)

            if target > matrix[mid][len(matrix[mid])-1]: 
                low = mid +1 

            if target < matrix[mid][0]:
                high = mid - 1

        return False


        