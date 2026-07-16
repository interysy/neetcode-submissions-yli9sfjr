# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = {}
        found_cycle = False

        while not found_cycle and head:
            hashed = hash(head) 

            if hashed in seen_nodes:
                found_cycle = True
                return True

            seen_nodes[hashed] = True
            head = head.next

        return False