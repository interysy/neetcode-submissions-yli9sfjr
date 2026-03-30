from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        doubles = defaultdict(type([]))
        length = len(nums)
        triples = []

        for i in range(length): 
            for j in range(length): 
                if i != j: 
                    if doubles.get((nums[i] + nums[j]), None) == None: 
                        doubles[(nums[i] + nums[j])] = []
                    else:
                        if sorted([i,j]) not in doubles[(nums[i] + nums[j])]:
                            doubles.get((nums[i] + nums[j]), []).append(sorted([i,j]))


        for index,num in enumerate(nums): 
            target = 0 - num
            if doubles.get(target,None) != None: 
                potentials = doubles[target] 
                for potential in potentials:
                    if index not in potential:
                        to_add =  sorted([num, nums[potential[0]] , nums[potential[1]]])
                        if to_add not in triples: 
                            triples.append(sorted([num, nums[potential[0]] , nums[potential[1]]]))
                
        return triples



        