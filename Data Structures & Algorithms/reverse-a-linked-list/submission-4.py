# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseLinkedList(self, previous_node , next_node): 

        if next_node == None:
            return previous_node 

        subsequent_node = next_node.next 
        next_node.next = previous_node

        return self.reverseLinkedList(next_node, subsequent_node)



    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return self.reverseLinkedList(None, head)



            
        