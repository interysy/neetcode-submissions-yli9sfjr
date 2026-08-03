"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        if not head: 
            return None

        dictionary = {}
        traversal_pointer = head
        while traversal_pointer: 
            dictionary[hash(traversal_pointer)] = Node(head.val)
            traversal_pointer = traversal_pointer.next

        new_list = dictionary[hash(head)]
        new_list_head = new_list
        # print(dictionary) 

        while head and new_list: 
            new_list.val = head.val
            new_list.next = dictionary.get(hash(head.next), None)
            new_list.random = dictionary.get(hash(head.random), None)

            # print("--------")
            # print(new_list.val)
            # print("--------")

            head = head.next 
            new_list = dictionary.get(hash(head), None)


        return new_list_head

        

            
            


        

        


        


        