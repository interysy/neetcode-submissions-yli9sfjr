from collections import defaultdict
import string

class Solution:

    def groupAnagrams(self, strs: List[str])-> List[List[str]]:

        groups = defaultdict(list)

        for element in strs: 
            alphabet_dict = {}


            for c in element: 
                if alphabet_dict.get(c) == None: 
                    alphabet_dict[c] = 1
                else: 
                    alphabet_dict[c] += 1

            print(alphabet_dict)
            
            groups[tuple(sorted(alphabet_dict.items()))].append(element)

        return list(groups.values())
