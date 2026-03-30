class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length_s = len(s)

        if length_s == 0 or length_s == 1: 
            return len(s) 

        start_index = 0 
        end_index = 1

        countmap = defaultdict(int)
        countmap[s[start_index]] = countmap.get(s[start_index] , 0) + 1 
        maximum = 1


        while end_index <= length_s - 1: 

            end_character = s[end_index]
            

            if countmap.get(end_character,None) == None or countmap[end_character] == 0: 
                countmap[end_character] = countmap.get(end_character,0) + 1
                end_index += 1
            else: 
                countmap[s[start_index]] -= 1 
                start_index += 1 
                continue


            difference = end_index - start_index

            if difference > maximum:
                maximum = difference



        final_string = s[start_index : end_index] 
        if len(final_string) < maximum:
             return maximum 
        else: 
            if len(set(final_string)) == len(final_string): 
                return len(final_string)
                


            




        