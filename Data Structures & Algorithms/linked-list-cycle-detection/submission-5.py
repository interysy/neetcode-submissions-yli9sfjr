# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False # Empty or single-node list has no cycle

        slow = head # Start slow pointer at head
        fast = head.next # Start fast pointer at head.next

        while fast and fast.next:
            slow = slow.next # Move slow pointer one step
            fast = fast.next.next # Move fast pointer two steps

            if slow == fast: # Pointers meet, cycle detected
                return True

        return False # Fast pointer reached the end, no cycle
