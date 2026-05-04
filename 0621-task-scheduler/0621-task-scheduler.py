class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = collections.Counter(tasks)

        freq_max_heap = []
        for freq in task_freq.values():
            freq_max_heap.append(-1*freq)
        
        heapq.heapify(freq_max_heap)

        max_freq= heapq.heappop(freq_max_heap)
        max_freq *= -1

        empty_spaces = (max_freq-1)*n
    

        while freq_max_heap:
            f = heapq.heappop(freq_max_heap)
            f *= -1
            
            empty_spaces -= min(f, max_freq-1)

        empty_spaces = max(0, empty_spaces)
        
        return len(tasks) + empty_spaces

