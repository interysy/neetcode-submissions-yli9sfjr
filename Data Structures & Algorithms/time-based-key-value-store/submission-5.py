from collections import defaultdict

class TimeMap:


    def binarySearch(self, arr , left, right, target): 

        current = ""
        while left <= right:
            mid = left + ((right - left) // 2) 
            stamp, value = arr[mid]

            if stamp == target: 
                return value
            
            if stamp > target: 
                right = mid - 1
            elif stamp < target: 
                left = mid + 1
                current = value
        
        return current

    # {key : [(stamp : value)]}
    def __init__(self):
        self.timemap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timemap.get(key, None) != None: 
            self.timemap[key].append((timestamp, value))
        else: 
            self.timemap[key] = [(timestamp, value)]

        return None

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap.get(key , None)

        if arr == None or len(arr) == 0: 
            return ""


        return self.binarySearch(arr, 0, len(arr) - 1 , timestamp)
