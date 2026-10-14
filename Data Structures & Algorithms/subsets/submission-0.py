class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        if len(nums) == 1: 
            return [[], [nums[0]]]

        res = [[]]

        def backtrack(current_set : list[int] = [], index : int = 0):
            # if iteration == len(nums): 
            #     return
            if index >= len(nums):
                return

            # print("running")


            for idx, element in enumerate(nums[index:]):
                if [element] not in res: 
                    res.append([element])

                current_set.append(element)
                # print(f"current set {current_set}")

                if current_set not in res: 
                    res.append(current_set.copy())
                    # print(f"added, so res {res}")
                backtrack(current_set.copy(),idx + index + 1)
                current_set.pop()

                
        backtrack()
        return res



        