class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums) - 1

        while left <= right: 
            mid = left + ((right - left) // 2)
            
            if right - left <= 2: 
                print(nums[left : right + 1])
                return min(nums[left:right+1])

            middle_element = nums[mid]
            left_element = nums[left]
            right_element = nums[right]

            # check left right
            # if 

            print("low " , left)
            print("middle " , mid)
            print("high " , right)


            # deflection point must be on the right 
            if left_element < middle_element and right_element < middle_element: 
                print("left segment sorted, take right")
                left = mid + 1

            if left_element < middle_element and right_element > middle_element:
                print("all sorted, take left") 
                right = mid - 1

            # you are at deflection point 
            if left_element > middle_element and right_element > middle_element: 
                print("left")
                right = mid

        return nums[left]
