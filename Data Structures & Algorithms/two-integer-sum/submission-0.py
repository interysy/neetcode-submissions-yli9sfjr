class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        for index, element in enumerate(nums): 
            for sub_index, sub_element in enumerate(nums[index+1:]):
                if element+sub_element == target: 
                    return [index, sub_index+index+1]




        