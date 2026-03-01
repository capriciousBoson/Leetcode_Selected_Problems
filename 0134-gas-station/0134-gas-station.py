class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g-c for g,c in zip(gas, cost)]

        if sum(diff) <0: return -1

        print(f"g : {gas}")
        print(f"c : {cost}")
        print(f"d : {diff}")

        total = 0
        res = 0
        for i,n in enumerate(diff):
            total += n
            if total <0:
                total = 0
                res = i+1
        return res


        