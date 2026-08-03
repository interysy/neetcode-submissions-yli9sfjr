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

        slow = head
        prev = slow
        fast = head.next
        difference = 1

        # print("Start slow" , slow.val)
        # print("Start fast " , fast.val)

        while fast:
            if difference != n: 
                # print("diff not equal")
                fast = fast.next 
                difference += 1 
                # print("Slow " , slow.val)
                # print("Fast ", fast.val)
            else: 
                # print("advancing")
                prev = slow
                fast = fast.next 
                slow = slow.next
                # pr/int("Slow " , slow.val)
                # print("Fast ", fast.val)

        
        prev.next = slow.next 
        if slow == head: 
            return slow.next
        return head


            



        # count from slow 
        # while difference between slow and fast is < n continue 
        # otherwise keep going going, once difference is greater then >n then update slow if fast.next is not none





        