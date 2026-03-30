class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        buckets = [set() for _ in range(len(nums))]


        for element in nums: 

            added = False
            # print(f"element {element}")

            for index, bucket in enumerate(buckets): 

                if added: 
                    # print("skipping")
                    break
                ## if not in any , then add to first 
                ## if in one, move up 
            

                if element in bucket: 
                    buckets[index + 1].add(element) 
                    buckets[index].remove(element)
                    # print(f"moving {element} from {index} to bucket {index+1}")
                    added = True
                    # print(buckets)
                    break



            if not added: 
                # print(f"adding {element} to bucket 0")
                buckets[0].add(element)
                # print(buckets)


        results = []
        for bucket in buckets[::-1]: 
            results.extend(bucket)

        return results[:k]




        