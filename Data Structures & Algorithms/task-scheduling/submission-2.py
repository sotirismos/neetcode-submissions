class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counter = {}
        for task in tasks:
            tasks_counter[task] = tasks_counter.get(task, 0) + 1
        
        tasks_heap = []
        for task, freq in tasks_counter.items():
            tasks_heap.append((-freq, task))
        
        heapq.heapify(tasks_heap)
        cooldown = deque()

        time = 0
        while tasks_heap or cooldown:
            if tasks_heap:
                freq, task = heapq.heappop(tasks_heap)        
                freq *= -1
                freq -= 1
                if freq > 0:
                    next_available_time = time + n + 1
                    cooldown.append((freq, task, next_available_time))

            time += 1
            
            if cooldown and time == cooldown[0][2]:
                freq, task, _ = cooldown.popleft()
                heapq.heappush(tasks_heap, (-freq, task))

        return time

