# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head: 
            return None 

        if not head.next and n == 1: 
            return None
        
        prev_pointer_1 = None
        pointer_1 = head 
        pointer_2 = head
        current_n = 0

        while pointer_2:
            pointer_2 = pointer_2.next

            current_n += 1 

            if current_n > n: 
                current_n -= 1
                prev_pointer_1 = pointer_1
                pointer_1 = pointer_1.next


        if prev_pointer_1 == None: 
            return pointer_1.next

        prev_pointer_1.next = pointer_1.next
        pointer_1.next = None 
        return head 
             