class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {} 
        for index,num in enumerate(numbers): 
            seen[num] = index

        for index,num in enumerate(numbers): 
            needed = target - num
            in_dict = seen.get(needed,None)
            if in_dict != None and index != in_dict: 
                if index > in_dict: 
                    return [in_dict+1, index+1]
                else: 
                    return [index+1, in_dict+1]


        