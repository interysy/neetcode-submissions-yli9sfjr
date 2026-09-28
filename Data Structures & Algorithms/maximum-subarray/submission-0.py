class Solution:
    def maxSubArray(self, nums: list[int]) -> int:


        # edge cases
        # array of 0 -> not possible
        # array of 1 -> return array 
        # array of 2 -> [0] vs [1] vs [0,1] sums -> pick biggest

        # approach 1
        # create each subarray sum and select biggest
        # for each element x
        # iterate over the array again from x onwards - call those y
        # calculate sum, if bigger store
        # O(n^2) solution, O(n) space 

        # approach 2 
        # 2d array
        # iterate over each element - x
        # in 2d array - update values for each cell in that column


        # O(n) time and O(n) space

        length = len(nums)

        if length == 1: 
            return nums[0]

        if length == 2: 
            first = nums[0]
            second = nums[1]

            greater = first if first > second else second

            if sum(nums) > greater: 
                return first + second
            else: 
                return greater


        running_sum = [nums[0]]

        for number in nums[1:]: 

            new_running_sum = running_sum[-1] + number

            if number > new_running_sum: 
                running_sum.append(number)
            else: 
                running_sum.append(new_running_sum)

        return max(running_sum)

        