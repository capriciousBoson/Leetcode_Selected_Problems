class DisjointSet:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.rank = {i:1 for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a,b):
        roota = self.find(a)
        rootb = self.find(b)

        if roota==rootb: return
        if self.rank[roota] > self.rank[rootb]:
            self.parent[rootb] = roota

        elif self.rank[roota] < self.rank[rootb]:
            self.parent[roota] = rootb
        else:
            self.parent[roota] = rootb
            self.rank[roota] += 1
    
class Solution:
    def allDivisors(self,n):
        divisors = set()
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                divisors.add(i)
                divisors.add(int(n/i))
        divisors.add(n)
        return divisors

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <2 :
            return True
        dj = DisjointSet(n)
        isFactorOf = collections.defaultdict(list)

        D = dict()

        for i in range(n):
            if nums[i]==1:
                return False
            if nums[i] not in D:
                d_ = self.allDivisors(nums[i])
                D[nums[i]] = d_
            divisors = D[nums[i]]
            # print(f"divisors of {nums[i]} : {divisors}")
            for d in divisors:
                isFactorOf[d].append(i)
        # print(f"isFactorOf : {isFactorOf}")

        for nghs in isFactorOf.values():
            start = nghs[0]
            for node in nghs[1:]:
                dj.union(start, node)
        
        root = dj.find(0)
        # print(f"root : {root}")
        for i in range(n):
            p  = dj.find(i)
            # print(f"root of nums[{i}] ({nums[i]}) = {p}")
            if p != root:
                return False
        return True


        