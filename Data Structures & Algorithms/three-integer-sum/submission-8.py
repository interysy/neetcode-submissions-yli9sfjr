from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        triples = []

        for i, num in enumerate(nums): 
            current = i + 1 
            end = len(nums) - 1

            while current < end:
                calculated_sum = num + nums[current] + nums[end]
                sorted_combination = sorted([num, nums[current], nums[end]]) 
                if (calculated_sum) == 0 and sorted_combination not in triples: 
                    triples.append(sorted_combination)
                    end -=1
                elif num + nums[current] + nums[end] > 0:
                    end -= 1 
                else: 
                    current += 1
                


        return triples


        