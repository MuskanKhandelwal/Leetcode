from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.l=OrderedDict()
        self.capacity=capacity
    
    def get(self, key: int) -> int:
        if key not in self.l:
            return -1
        self.l.move_to_end(key)
        return self.l[key]

    def put(self, key: int, value: int) -> None:
        if key in self.l:
            del self.l[key]
        elif len(self.l) == self.capacity:
            self.l.popitem(last=False)
        self.l[key] = value
    
