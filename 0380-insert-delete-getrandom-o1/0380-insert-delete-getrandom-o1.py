import random
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.values_dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present. 
        Returns true if the item was not present, false otherwise.
        """
        if val in self.values_dict:
            return False
        self.values.append(val)
        self.values_dict[val] = len(self.values) -1

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. 
        Returns true if the item was present, false otherwise.
        """
        if val not in self.values_dict:
            return False

        index = self.values_dict[val]
        last = self.values[-1]

        self.values[index] = last
        self.values_dict[last] = index
        self.values.pop()

        del self.values_dict[val]
        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements
        (it's guaranteed that at least one element exists when this method is called)
        Each element must have the same probability of being returned.
        """
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()