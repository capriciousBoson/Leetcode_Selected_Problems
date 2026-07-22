class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = collections.Counter(s)


        print(f"counter : {freq}")
        heap = []
        for char, f in freq.items():
            heapq.heappush(heap, (-1*f, char))

        remaining_chars = len(s)
        res = ""
        
        while heap:
            f, char = heapq.heappop(heap)

            hold = ()
            if res and res[-1]==char:
                hold = (f,char)

            if len(hold):
                if heap:
                    f,char = heapq.heappop(heap)
                else:
                    return ""
            
            res = res+char
            f = f+1

            if f<0:
                heapq.heappush(heap, (f,char))
            if len(hold):
                heapq.heappush(heap, hold)

        return res


        