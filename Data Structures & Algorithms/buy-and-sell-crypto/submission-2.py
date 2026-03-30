import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buying_price = prices[0]
        maximum = 0
        for selling_price in prices: 
            calculated_price = selling_price - buying_price
            if calculated_price > maximum: 
                maximum = calculated_price 

            if selling_price < buying_price: 
                buying_price = selling_price


        return maximum
            




       




        