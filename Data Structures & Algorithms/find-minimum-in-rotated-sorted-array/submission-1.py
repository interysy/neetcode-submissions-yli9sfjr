class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums) - 1

        while left < right: 
            mid = left + ((right - left) // 2)

            middle_element = nums[mid]
            left_element = nums[left]
            right_element = nums[right]

            if middle_element < right_element: 
                right = mid
            else: 
                left = mid + 1

        return nums[left]
