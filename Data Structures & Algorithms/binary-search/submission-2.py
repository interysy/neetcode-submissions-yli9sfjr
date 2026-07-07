class Solution:


    def binarySearch(self, nums : List[int], low : int, high : int, target : int) -> int:

        mid = low + ((high-low) // 2)

        if low > high: 
            return -1

        if nums[mid] == target: 
            return mid 

        if nums[mid] > target: 
            return self.binarySearch(nums, low , mid - 1, target)

        if nums[mid] < target: 
            return self.binarySearch(nums, mid + 1, high, target)


    def search(self, nums: List[int], target: int) -> int:

        return self.binarySearch(nums, 0, len(nums) - 1, target)

    

        
        