class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}
        for task in tasks:
            if task in task_freq:
                task_freq[task] += 1
            else:
                task_freq[task] = 1

        time = 0
        task_freqs = [(-freq, task) for task, freq in task_freq.items()]
        heapq.heapify(task_freqs)
        cooldown_queue = deque()

        while task_freqs or cooldown_queue:
            if task_freqs:
                task_freq, task = heapq.heappop(task_freqs)
                task_freq *= -1
                task_freq -= 1
                if task_freq > 0:
                    next_available_time = time + n + 1
                    cooldown_queue.append((task, task_freq, next_available_time))
            time += 1

            if cooldown_queue and cooldown_queue[0][2] == time:
                task, task_freq, next_available_time = cooldown_queue.popleft()
                heapq.heappush(task_freqs, (-task_freq, task))
        
        return time
        