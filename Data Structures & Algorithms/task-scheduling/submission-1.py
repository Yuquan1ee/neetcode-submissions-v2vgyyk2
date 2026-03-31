class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a heap to store the last n task
        # use a hash map to store the last n task for look up
        freq_map = [(-tasks.count(i), i) for i in set(tasks)] #(negative_freq, letter)
        heapq.heapify(freq_map)
        last_n = [] # (counter, negative_frequency, letter)
        counter = 1
        heapq.heapify(last_n)
        while(freq_map or last_n):
            print(f"{freq_map}")
            print(f"{last_n}")
            if len(last_n)>0:
                if last_n[0][0] + n < counter:
                    removed = heapq.heappop(last_n)
                    heapq.heappush(freq_map, (removed[1], removed[2]))
            
            if not freq_map:
                counter += 1
            else:
                cur = heapq.heappop(freq_map)    
                if cur[0] != -1:
                    heapq.heappush(last_n, (counter,cur[0]+1, cur[1]))
                counter += 1

        return counter -1





