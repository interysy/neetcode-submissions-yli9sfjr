from typing import Optional

class Node: 
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value 
        self.next_node: Optional['Node'] = None
        self.prev_node: Optional['Node'] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pointers = {}  # key -> Node
        
        # Dummy head and tail nodes isolate boundary conditions
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def _remove(self, node: Node) -> None:
        """Disconnects an existing node from the list."""
        prev = node.prev_node
        nxt = node.next_node
        prev.next_node = nxt
        nxt.prev_node = prev

    def _add_to_front(self, node: Node) -> None:
        """Inserts a node right after dummy head (Most Recently Used)."""
        node.prev_node = self.head
        node.next_node = self.head.next_node
        self.head.next_node.prev_node = node
        self.head.next_node = node

    def get(self, key: int) -> int:
        if key not in self.pointers:
            return -1
        
        node = self.pointers[key]
        # Move accessed node to MRU position
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            # Update existing value and refresh position
            node = self.pointers[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Evict LRU node if capacity reached
            if len(self.pointers) >= self.capacity:
                lru_node = self.tail.prev_node  # Node right before dummy tail
                self._remove(lru_node)
                del self.pointers[lru_node.key]
            
            # Insert new node
            new_node = Node(key, value)
            self.pointers[key] = new_node
            self._add_to_front(new_node)