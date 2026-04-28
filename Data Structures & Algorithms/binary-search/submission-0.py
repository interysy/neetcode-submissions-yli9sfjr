import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:



        start = 0 
        end = len(nums) - 1
        its = 5
        
        while start <= end: 
            pivot = math.ceil((end - start) // 2) + start

            ##print(f"pivot {pivot} is {nums[pivot]}")
            #print(f"looking at {nums[start:end+1]}")


            if nums[pivot] == target: 
             #   print(f"found at {target}")
                return pivot 

            if nums[pivot] < target: 
                start = pivot + 1
            else: 
                end = pivot - 1



        return -1


        