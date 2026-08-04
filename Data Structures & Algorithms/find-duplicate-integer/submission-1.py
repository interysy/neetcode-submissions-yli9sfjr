class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_index = nums[0]
        fast_index = nums[nums[0]]


        while fast_index != slow_index: 
            slow_index = nums[slow_index]
            fast_index = nums[nums[fast_index]]


        slow_index_2 = 0
        while slow_index_2 != slow_index:
            slow_index = nums[slow_index]
            slow_index_2 = nums[slow_index_2]


        return slow_index
        