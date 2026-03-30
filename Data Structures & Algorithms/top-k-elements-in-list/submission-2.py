from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = defaultdict(set)


        for element in nums: 

            added = False

            for key, bucket in buckets.items():     
                if element in bucket: 
                    buckets[key + 1].add(element) 
                    buckets[key].remove(element)
                    added = True
                    break

            if not added: 
                buckets[0].add(element)



        results = []
        # reversed() is more memory-efficient than [::-1]
        for bucket in reversed(buckets.values()):
            if bucket:
                results.extend(bucket)
            if len(results) >= k:
                break

        return results[:k]




        