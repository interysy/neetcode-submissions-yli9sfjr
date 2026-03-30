class Solution:
    def characterReplacement(self, s: str, k : int) -> int:

        length_s = len(s)
        if length_s == 0 or length_s == 1: 
            return len(s) 

        start_index = 0 
        maximum = 0 
        countmap = defaultdict(int)

        for end_index in range(len(s)): 
            print(f"current end {end_index} with {s[start_index:end_index+1]}")
            countmap[s[end_index]] = countmap.get(s[end_index] , 0) + 1

            ## check valid
            while ((end_index - start_index + 1) - max(countmap.values())) > k: 
                print("invalid moving start")
                countmap[s[start_index]] -= 1
                start_index += 1
                

            ## update our maximum 
            maximum = max(maximum, end_index - start_index + 1)


        return maximum

            

                

    