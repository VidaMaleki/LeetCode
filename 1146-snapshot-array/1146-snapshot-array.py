class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        history = self.arr[index]

        if history[-1][0] == self.snap_id:
            history[-1][1] = val
        else:
            history.append([self.snap_id, val])

    def snap(self) -> int:
        s_id = self.snap_id
        self.snap_id += 1
        return s_id

    def get(self, index: int, snap_id: int) -> int:
        history = self.arr[index]  # sorted by snap_id
        
        lo, hi = 0, len(history) - 1
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if history[mid][0] <= snap_id:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return history[ans][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)