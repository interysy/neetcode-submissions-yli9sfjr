import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = [1] 
        suffix = [1]
        output = [1] * len(nums)
        
        for index,element in enumerate(nums[:-1]):

            # print(f"looking at {element}")

            # print(f"for prefix {prefix[index-1]} * {element}")
            prefix.append(prefix[index] * element)
            suffix.append(suffix[index] * nums[len(nums) - 1 - index])

        #     print(prefix)

        # print(suffix)

        for i in range(len(nums)): 
            output[i] = prefix[i] * suffix[len(nums)-1-i]


        return output







        #     for sub_index, sub_item in enumerate(nums): 
        #         if index == sub_index: 
        #             continue 

        #         output[index] = output[index] * sub_item


        # return output
