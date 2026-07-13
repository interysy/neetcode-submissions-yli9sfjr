from collections import defaultdict

class TimeMap:


    def binarySearchExact(self, arr , left, right, target): 

        while left <= right:
            mid = left + ((right - left) // 2) 

            # print(arr)
            stamp, value = arr[mid]

            if stamp == target: 
                return value
            
            if stamp > target: 
                right = mid - 1
            elif stamp < target: 
                left = mid + 1
        
        return None


    def binarySearchRange(self, arr, left, right, target): 
        print("range")
        current = None
        while left <= right:

            print("left " , left)
            print("right " , right)

            mid = left + ((right - left) // 2) 

           
            print(mid)
            # print(arr[left : right + 1])
            stamp, value = arr[mid]

            if stamp <= target: 
                print("smaller take right")
                left = mid + 1
                current = value
            elif stamp > target: 
                print("bigger take left")
                right = mid - 1
           
        
        return current

    # {key : [(stamp : value)]}
    def __init__(self):
        self.timemap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # print("setting")
        if self.timemap.get(key, None) != None: 
            self.timemap[key].append((timestamp, value))
        else: 
            self.timemap[key] = [(timestamp, value)]

        # print("timemap " , self.timemap)
        return None

    def get(self, key: str, timestamp: int) -> str:
        # print("getting")
        arr = self.timemap.get(key , None)
        # print("curren arr " , self.timemap )

        if arr == None or len(arr) == 0: 
            return ""

        # print("here")

        value = self.binarySearchExact(arr, 0, len(arr) - 1 , timestamp)

        print("value found " , value)
        print("type valiue " , type(value))

        if value == None: 
            print("returning default")
            default = self.binarySearchRange(arr, 0, len(arr) - 1 , timestamp)
            print("default is " , default)
            if default == None: 
                return ""
            return default 

        return value