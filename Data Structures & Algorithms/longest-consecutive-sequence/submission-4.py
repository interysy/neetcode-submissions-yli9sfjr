
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        if len(nums) < 1: 
            return len(nums)

        # print(nums)
        starters = set() 

        for num in nums: 
            if (num-1) not in nums: 
                starters.add(num)


        maximum = 1
        for starter in starters: 
            amount = 1
            # print(f"starter {starter}")
            while starter+amount in nums: 
                amount+=1
                # print(f"checking next and adding 1")

            if amount > maximum: 
                # print(f"new max {amount}")
                maximum = amount


        return maximum



        