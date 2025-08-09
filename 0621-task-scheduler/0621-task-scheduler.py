from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        # freq = [item[1] for item in sorted(c.items(), key=lambda x: x[1])]
        freq = []
        for task, f in c.items():
            heapq.heappush(freq, -1*f)
        # print(freq)
        f1 = -1*heapq.heappop(freq)
        extra_places = (f1 - 1)*n

        # print(f"f1 = {f1}, extraplaces = {extra_places}")
        while freq:
            f = -1*heapq.heappop(freq)
            # print(f"current frequency = {f}, occ = { min(f1-1, f)} ")

            extra_places -= min(f1-1, f)
        # print(f"finally extra_places : {extra_places}")
        return len(tasks) + max(0, extra_places)

        