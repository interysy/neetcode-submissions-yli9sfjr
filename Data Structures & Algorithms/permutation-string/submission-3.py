class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # sliding window approach 
        countmap = defaultdict(int)

        for char in s1: 
            countmap[char] = countmap.get(char,0) + 1
        
        start_index = 0 
        end_index = 0
        to_consider = sum([value for value in countmap.values()])

        print(to_consider)

        while end_index < len(s2): 
            end_character = s2[end_index] 

            print(f"considering {s2[start_index : end_index + 1]}")
            print(countmap)

            if countmap.get(end_character,0) != 0: 
                print("in")
                countmap[end_character] -= 1    
                to_consider -= 1
                end_index += 1
            else:
                print("out")

                if start_index == end_index: 
                    end_index += 1 

                if countmap.get(s2[start_index] , None) != None:
                    countmap[s2[start_index]] += 1
                    to_consider += 1
                start_index += 1 

            
               


            print(to_consider)
            if to_consider <= 0: 
                
                return True 


        return False


        
        