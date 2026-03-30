import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        prices_2d = np.tile(prices, (len(prices), 1))

        summed = prices_2d - np.transpose(prices_2d)
        summed = np.triu(summed)
        maximum = np.max(summed)
        


        return int(maximum)



       




        