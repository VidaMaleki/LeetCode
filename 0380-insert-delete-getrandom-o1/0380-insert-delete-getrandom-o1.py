import random
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.values_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.values_dict:
            return False
        self.values.append(val)   
        self.values_dict[val] = len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_dict:
            return False
        
        index = self.values_dict[val]
        last = self.values[-1]

        # [1, 3, 7] -> [1, 7, 7]
        self.values[index] = last
        self.values_dict[last] = index
        self.values.pop()

        del self.values_dict[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()