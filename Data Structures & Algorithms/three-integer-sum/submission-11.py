from collections import defaultdict
from itertools import chain 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums) 
        length = len(nums)
        triples = defaultdict(list)

        seen = set()
        for index,num in enumerate(nums): 
            start = index + 1 
            end = length - 1
            while start < end:

                # print(f"current {index} with {num}")
                # print(f"start {start} with {nums[start]}")
                # print(f"end {end} with {nums[end]}")
                calculated_sum = num + nums[start] + nums[end]
                # print(f"calculated {calculated_sum}")
                if calculated_sum > 0: 
                    # print("LESS required")
                    end = end -  1
                elif calculated_sum < 0: 
                    # print("MORE required")
                    start = start + 1
                else:
                    # print("EQUAL")
                    sorted_key = tuple(sorted([index, start, end]))
                    if sorted_key not in triples and tuple([num,nums[start],nums[end]]) not in seen: 
                        # print(f"added {sorted_key} with {[num, nums[index],nums[end]]}")
                        triples[sorted_key].append([num,nums[start],nums[end]])
                        seen.add(tuple([num,nums[start],nums[end]]))

                    end = end - 1
                    # sorted_key = tuple(sorted([index, start, end]))
                    # if sorted_key not in triples: 
                    #     triples[sorted_key].append([num, nums[index],nums[end]])

        # print(triples)
        
        return list(chain.from_iterable(triples.values()))




        