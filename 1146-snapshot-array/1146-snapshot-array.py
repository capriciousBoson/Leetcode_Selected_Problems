class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{0:0} for _ in range(length)]
        # self.snapshots = {}
        self.snaps = 0
        

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snaps] = val
        

    def snap(self) -> int:

        # self.snapshots[self.snaps] = [n for n in self.arr]
        self.snaps += 1
        return self.snaps -1

        

    def get(self, index: int, snap_id: int) -> int:
        s = snap_id
        while s not in self.arr[index]:
            s -= 1

        return self.arr[index][s]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)