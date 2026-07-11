
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        heap = [(-c, ch) for ch, c in hashmap.items()]
        heapq.heapify(heap)

        queue = collections.deque()
        time = 0

        while heap or queue:
            time += 1

            if queue and queue[0][0] == time:
                _, count, ch = queue.popleft()
                heapq.heappush(heap, (count, ch))

            if heap:
                count, ch = heapq.heappop(heap)
                count += 1
                if count < 0: 
                    queue.append((time+n+1, count, ch))
            
        return time