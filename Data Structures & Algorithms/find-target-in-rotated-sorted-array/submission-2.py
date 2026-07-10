class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left < right: 
            mid = left + ((right - left ) // 2)
            
            left_element = nums[left] 
            right_element = nums[right] 
            middle_element = nums[mid]

            if middle_element == target: 
                return mid 
            if left_element == target: 
                return left 
            if right_element == target: 
                return right

            # identify sorted 
            # check range of sorted segment

            if middle_element < right_element: 
                # right segment is sorted, so check range
                if target > middle_element and target < right_element: 
                    left = mid + 1
                else:
                    right = mid - 1
            elif left_element < middle_element: 
                # left segment is sorted, check range
                if target < middle_element and target > left_element: 
                    right = mid -1
                else:
                    left = mid +1
            else: 
                return -1


        if nums[left] == target: 
            return left
        

        return -1 
