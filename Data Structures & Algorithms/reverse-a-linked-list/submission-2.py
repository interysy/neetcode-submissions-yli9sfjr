# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None: 
            return None

        current = head 
        nodes = []
        while current.next != None: 
            nodes.append(current)
            current = current.next

        nodes.append(current)

        for i in range(len(nodes)-1 , -1, -1): 
            node = nodes[i]
            if i == 0: 
                node.next = None
            else:
                node.next = nodes[i-1]

        
        return nodes[-1]



            
        