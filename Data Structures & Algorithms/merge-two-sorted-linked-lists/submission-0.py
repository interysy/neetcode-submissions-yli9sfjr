# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if not list1: 
            return list2 

        if not list2: 
            return list1
            
        pointer_1 = list1
        pointer_2 = list2
        sorted_list = None
        sorted_head = None

        while pointer_1 or pointer_2: 

            if pointer_1 == None:
                sorted_list.next = pointer_2
                sorted_list = pointer_2
                pointer_2 = pointer_2.next
                continue 

            if pointer_2 == None: 
                sorted_list.next = pointer_1
                sorted_list = pointer_1
                pointer_1 = pointer_1.next
                continue


            if pointer_1.val <= pointer_2.val: 
                if sorted_head == None: 
                    sorted_head = pointer_1
                    sorted_list = pointer_1 
                else: 
                    sorted_list.next = pointer_1 
                    sorted_list = pointer_1
                pointer_1 = pointer_1.next
            else: 
                if sorted_head == None: 
                    sorted_head = pointer_2
                    sorted_list = pointer_2
                else: 
                    sorted_list.next = pointer_2
                    sorted_list = pointer_2 
                pointer_2 = pointer_2.next

        return sorted_head
                
                 
        