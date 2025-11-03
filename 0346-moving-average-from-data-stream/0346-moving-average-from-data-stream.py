class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue =  [0]* size
        self.count = 0
        self.sum_so_far = 0
        self.index = 0

    def next(self, val: int) -> float:
        if self.size == self.count:
            self.sum_so_far -= self.queue[self.index]
        else:
            self.count +=1
        self.sum_so_far += val
        self.queue[self.index] = val
        self.index = (self.index +1 ) % self.size
        
        return self.sum_so_far / self.count
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)