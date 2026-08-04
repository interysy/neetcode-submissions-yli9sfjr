# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()
        traversal = new_head
        carry = 0 
        while l1 or l2 or carry != 0:

            if not l1: 
                l1_value = 0
            else: 
                l1_value = l1.val

            if not l2: 
                l2_value = 0
            else: 
                l2_value = l2.val


            result = l1_value + l2_value + carry

            value = result % 10 
            carry = result // 10

            traversal.next = ListNode(value)
            traversal = traversal.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return new_head.next





        