class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triples = []
        end_index = len(nums) - 1
        
        while end_index != 0:
            for start_index, start_element in enumerate(nums): 
                # print(f"START INDEX {start_index} START ELEMENT {start_element}")
                current_index = end_index - 1
                # print(f"END INDEX {end_index} END ELEMENT {nums[end_index]}")
                while current_index > start_index: 
                    element = nums[current_index]
                    # print(f"CURRENT_INDEX {current_index} CURRENT ELEMENT {element}")
                    if (start_element + element + nums[end_index]) == 0 and sorted([start_element, element,nums[end_index]]) not in triples:
                        # print(f"adding indexes {start_index} {current_index} {end_index}")
                        triples.append(sorted([start_element, element,nums[end_index]])) 
                    current_index -= 1
            end_index -=1


        return triples




        