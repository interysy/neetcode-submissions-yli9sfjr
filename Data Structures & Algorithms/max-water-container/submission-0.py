class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0 
        end = len(heights) - 1
        maximum = 0


        while start < end: 
            amount = (end-start)* min(heights[start], heights[end])

            print(f"amount {amount}")

            if amount > maximum: 
                maximum = amount

            if heights[start] > heights[end]: 
                end -= 1
            else: 
                start += 1


        return maximum


        