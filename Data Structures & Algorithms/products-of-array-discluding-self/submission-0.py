class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        output = [1] * len(nums)
        for index, item in enumerate(nums):
            for sub_index, sub_item in enumerate(nums): 
                if index == sub_index: 
                    continue 

                output[index] = output[index] * sub_item


        return output
