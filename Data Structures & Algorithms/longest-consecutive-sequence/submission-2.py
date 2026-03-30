
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        if len(nums) == 1: 
            return 1

        count = {}

        for num in nums: 
            count[num] = 0


        seen = set()
        for num in nums: 
            if count.get(num+1,None) != None and num not in seen: 
                count[num] += 1 
            seen.add(num)

        maximum = 0
        for key, val in count.items(): 
            looking = True 
            current = 1
            i = 1
            while count.get(key+i,0) == 1: 
                i += 1
            if i+1> maximum: 
                maximum = i+1



        return maximum



        