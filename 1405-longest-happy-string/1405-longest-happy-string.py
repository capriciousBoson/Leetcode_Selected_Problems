class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {}
        if a:
            counts['a']=a
        if b:
            counts['b']=b
        if c:
            counts['c']=c
        
        heap = []
        for char, f in counts.items():
            heapq.heappush(heap, (-f, char))

        res = ""
        while heap:
            print(f"\nres= {res}")
            f, char = heapq.heappop(heap)
            print(f"freq, char : {f,char}")
            hold = ()
            if res and  res[-1]== char:
                hold = (f,char)
                if heap:
                    f,char = heapq.heappop(heap)
                else:
                    continue


            f *= -1

            if len(hold) or f==1:
                res = res + char
                f -=1
            elif f>=2:
                res = res + char+char
                f -= 2

            print(f"updated res = {res}")
            if f:
                heapq.heappush(heap, (-f, char))

            if len(hold):
                heapq.heappush(heap, hold)

        return res
        