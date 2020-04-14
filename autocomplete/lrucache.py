from threading import Lock
from typing import List

class LRUCache():
    class Node(): 
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    def _move_to_top(self, node: Node):
        if self.head and self.head.key == node.key:
            return
        node.next.prev = node.prev
        if self.tail and node.key == self.tail.key:
            self.tail = node.next
        if node.prev:
            node.prev.next = node.next
        node.next = None
        node.prev = self.head
        self.head.next = node
        self.head = node

    def _pop(self) -> Node:
        node = self.tail
        self.tail = self.tail.next
        return node
        
    def _push(self, node):
        if not self.head or not self.tail:
            self.head = node
            self.tail = node
            return
        self.head.next = node
        node.prev = self.head
        self.head = node

    def __init__(self, capacity: int, seed: List[str]):
        assert capacity > 0, "Capacity must be > 0"
        self.cache = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.mutex = Lock()
        for s in seed:
            self.put(s)
  
    def put(self, key: str):
        self.mutex.acquire()
        if key in self.cache:
            node = self.cache[key]
            self._move_to_top(node)
        else:
            node = self.Node(key)
            self.cache[key] = node
            self._push(node)
            
            if len(self.cache) > self.capacity:
                popped = self._pop()
                del self.cache[popped.key]
                self.mutex.release()
                return popped.key 
        self.mutex.release()
        return None
