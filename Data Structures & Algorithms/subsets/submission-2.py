class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        if len(nums) == 1: 
            return [[], [nums[0]]]

        res = []
        current_set = []

        def backtrack(index : int = 0):
            if index >= len(nums):
                res.append(current_set.copy())
                return

            # include
            current_set.append(nums[index])
            backtrack(index+1)

            # not include 
            current_set.pop()
            backtrack(index+1)
                
        backtrack()
        return res



        