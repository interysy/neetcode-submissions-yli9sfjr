
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        if len(nums) < 1: 
            return len(nums)

        maximum = 0

        for num in nums: 
            if (num-1) not in nums: 
                amount = 1
                while num+amount in nums: 
                    amount+=1
                maximum = max(amount,maximum)
                

        return maximum



        