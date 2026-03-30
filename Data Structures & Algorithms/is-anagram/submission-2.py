from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = sorted(s) 
        t = sorted(t)  

        if len(t) != len(s): 
            return False 

        for i in range(len(s)): 
            if s[i] != t[i]: 
                return False

        return True

        # for i in range


        # s_characters = defaultdict(int) 
        # t_characters = defaultdict(int)

        # for i in range(max(len(s) , len(t))): 
        #     s_character == None 
        #     t_character = None

        #     if i < len(s): 
        #         s_character = s[i]
        #         s_characters[s_character] += 1

        #     if i < len(t): 
        #         t_character = t[i]
        #         t_characters[t_character] += 1



        f
            

            

            

        if len(s_set.union(t_set)) == len(s_set): 
            return True

        return False
        