class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        free = []
        for i in range(n):
            heapq.heappush(free, [i, 0])
        busy = []
        counts = [0 for _ in range(n)]

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                e,r = heapq.heappop(busy)
                heapq.heappush(free, [r, e] )
            
            if free:
                r , e = heapq.heappop(free)
            else:
                e, r = heapq.heappop(busy)

            new_end_time = end

            if e > start:
                duration = end - start
                new_end_time = e + duration

            heapq.heappush(busy, [new_end_time, r])
            counts[r] +=1

        print(f"counts : {counts}")
        max_rooms = max(counts)
        for i,c in enumerate(counts):
            if c==max_rooms:
                return i
            

            
