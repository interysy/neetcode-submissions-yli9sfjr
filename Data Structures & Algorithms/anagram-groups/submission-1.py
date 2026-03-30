from collections import defaultdict
import string

class Solution:

    def groupAnagrams(self, strs: List[str])-> List[List[str]]:

        groups = defaultdict(list)

        for element in strs: 
            alphabet_dict = [0]*26


            for c in element: 
                alphabet_dict[ord('a') - ord(c)] += 1

            
            groups[tuple(alphabet_dict)].append(element)

        return list(groups.values())

            




        