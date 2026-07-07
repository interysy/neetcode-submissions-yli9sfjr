class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0 
        high = len(nums) - 1

        while low <= high: 
            mid = low + ((high - low) // 2)
            mid_number = nums[mid]

            if mid_number == target: 
                return mid 


            if mid_number > target: 
                high = mid - 1

            if mid_number < target: 
                low = mid + 1


        return -1 

        
        