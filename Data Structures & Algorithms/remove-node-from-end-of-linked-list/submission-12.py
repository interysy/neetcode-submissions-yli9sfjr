# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None 

        if not head.next:
            if  n == 1: 
                return None 
            else: 
                return head


        if not head.next.next:  
            if n == 1: 
                head.next = None
                return head 
            elif n == 2: 
                return head.next

        
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head
        difference = 1
        

        while fast.next:
            if difference != n: 
                fast = fast.next 
                difference += 1 
            else: 
                prev = slow
                fast = fast.next 
                slow = slow.next

        
        slow.next = slow.next.next
        return dummy.next


            



        # count from slow 
        # while difference between slow and fast is < n continue 
        # otherwise keep going going, once difference is greater then >n then update slow if fast.next is not none





        