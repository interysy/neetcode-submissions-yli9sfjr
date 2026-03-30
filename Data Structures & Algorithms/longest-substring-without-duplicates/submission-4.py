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

            # print(f"CURRENT string {s[start_index : end_index+1]}")
            # print(f"start index {start_index}")
            # print(f"end index {end_index}")

            end_character = s[end_index]

            # print(countmap)

            # print(end_character)
            

            if countmap.get(end_character,None) == None or countmap[end_character] == 0: 
                countmap[end_character] = countmap.get(end_character,0) + 1
                end_index += 1
                # print("extending")
            else: 
                # print("shortening")
                countmap[s[start_index]] -= 1 
                start_index += 1 
                continue


            difference = end_index - start_index

            if difference > maximum:
                # print("updating") 
                maximum = difference


        if len(set(s[start_index:end_index])) == len(s[start_index:end_index]): 
            if len(s[start_index:end_index]) > maximum: 
                maximum = len(s[start_index:end_index])



        return maximum
            


            




        