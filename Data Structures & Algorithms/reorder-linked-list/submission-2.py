# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return 

        reversed_nodes = []
        last = head
        while last: 
            reversed_nodes.append(last)
            last = last.next
    
        last = reversed_nodes[-1]

        left = reversed_nodes[0]
        right = reversed_nodes[-1]

        curr_right = len(reversed_nodes) - 1
        curr_left = 0

        while curr_left < curr_right: 
            temp = left.next
            left.next = right
            right.next = temp

            curr_right -= 1
            curr_left += 1
            
            right = reversed_nodes[curr_right]
            left = reversed_nodes[curr_left]

        left.next = None

        
        


             

        