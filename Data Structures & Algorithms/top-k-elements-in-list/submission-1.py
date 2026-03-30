class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        buckets = [set() for _ in range(len(nums))]


        for element in nums: 

            added = False

            for index, bucket in enumerate(buckets):     
                if element in bucket: 
                    buckets[index + 1].add(element) 
                    buckets[index].remove(element)
                    added = True
                    break

            if not added: 
                buckets[0].add(element)


        results = []
        length = 0
        while length < k: 
            for bucket in buckets[::-1]: 
                results.extend(bucket)
                length = length + len(bucket)

        return results[:k]




        