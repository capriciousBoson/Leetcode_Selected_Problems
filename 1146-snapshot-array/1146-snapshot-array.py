from bisect import bisect_right
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{0:0} for _ in range(length)]
        # self.snapshots = {}
        self.snaps = 0
        # self.last_added_snap = 0
        

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snaps] = val
        # self.last_added_snap = self.snaps
        

    def snap(self) -> int:

        # self.snapshots[self.snaps] = [n for n in self.arr]
        self.snaps += 1
        return self.snaps -1

        

    def get(self, index: int, snap_id: int) -> int:
        keys = sorted(self.arr[index].keys())         # snap_ids where this index changed
        pos = bisect_right(keys, snap_id) - 1 

        return self.arr[index][keys[pos]]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)