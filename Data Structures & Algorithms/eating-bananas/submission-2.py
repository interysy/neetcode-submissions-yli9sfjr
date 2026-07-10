import math 
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == 1: 
            return math.ceil(piles[0] / h)

        piles = sorted(piles)

        print(piles)

        highest_rate = max(piles)
        lowest_rate = 1 


        low = 0
        high =  highest_rate - 1 
        current_answer = highest_rate

        while low <= high and high != 0: 
            print("low " , low)
            print("high ", high)
            midpoint = low + ((high-low) //2) 
            print("mid " , midpoint)
            print("midpoint " , midpoint + 1)

            time = sum([math.ceil(pile / (midpoint+1)) for pile in piles])


            print("total time " ,  time)

            if time > h: 
                print("out of range, look at left half")
                low = midpoint + 1
            else: 
                print("correct, set answer, look at right half to optimise")
                current_answer = midpoint + 1
                high = midpoint - 1


        return current_answer



        