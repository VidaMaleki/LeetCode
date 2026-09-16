from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cashe = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cashe:
            return -1
        self.cashe.move_to_end(key)
        return self.cashe[key]
    

    def put(self, key: int, value: int) -> None:
        if key in self.cashe:
            self.cashe[key] = value
            self.cashe.move_to_end(key)
        else:
            if len(self.cashe) >= self.capacity:
                self.cashe.popitem(last=False)
            self.cashe[key] = value
        return self.cashe
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)