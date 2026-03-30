class MinStack:

    stack = []
    minimum_stack = [] 

    def __init__(self):
        self.stack = []
        self.minimum_stack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        # print(f"ADDING {val}")
        if len(self.minimum_stack) == 0 or val < self.minimum_stack[-1]: 
            # print("new min")
            self.minimum_stack.append(val)
        else: 
            # print("old min")
            self.minimum_stack.append(self.minimum_stack[-1])

        # print(self.stack)
        # print(self.minimum_stack)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum_stack[-1]


        
## what if min element gets removed? then I need to search stack no? 