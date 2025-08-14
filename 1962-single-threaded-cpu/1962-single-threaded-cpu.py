from collections import defaultdict
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        min_heap = []
        tasks = [[t[0],t[1],i,] for i, t in enumerate(tasks)]
        tasks.sort(key=lambda x : x[0])

        time = 0
        i = 0
        res = []
        # print(f"tasks : {tasks}")

        while i < n or min_heap:
            if not min_heap and time < tasks[i][0]:
                time = tasks[i][0]
            # print(f"\ntime : {time} i : {i} , res : {res}")
            while i< n and tasks[i][0] <= time:
                heapq.heappush(min_heap,(tasks[i][1], tasks[i][2]))
                i += 1
            # print(f"enqued tasks  :{min_heap}")
            if min_heap:
                processing_time, index = heapq.heappop(min_heap)
                res.append(index)
                time += processing_time
        return res

        