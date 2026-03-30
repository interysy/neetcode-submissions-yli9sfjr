import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = np.ones(len(nums))
        print(output)
        
        for index, item in enumerate(nums):
            mask = np.ones(len(nums), dtype=bool)
            mask[index] = False 
            output[mask] *= item
            print(output)

        return output.astype(int).tolist()







        #     for sub_index, sub_item in enumerate(nums): 
        #         if index == sub_index: 
        #             continue 

        #         output[index] = output[index] * sub_item


        # return output
