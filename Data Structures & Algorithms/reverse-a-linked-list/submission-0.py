# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # follow pointer till end, store reference to each node? 
        # iterate backwards, update pointer? 

        if head == None: 
            return None

        current = head 
        nodes = []
        while current.next != None: 
            nodes.append(current)
            current = current.next

        nodes.append(current)

        nodes = nodes[::-1]
        print([node.val for node in nodes])

        for index, node in enumerate(nodes): 
            if index == (len(nodes)-1): 
                node.next = None
            else:
                node.next = nodes[index+1]

        
        return nodes[0]



            
        