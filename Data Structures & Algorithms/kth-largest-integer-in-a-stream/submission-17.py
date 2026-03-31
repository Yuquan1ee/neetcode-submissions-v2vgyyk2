import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.length = len(nums)
        while(self.length > k):
            heapq.heappop(self.min_heap)
            self.length -= 1


    def add(self, val: int) -> int:
        if self.length == self.k:
            heapq.heappushpop(self.min_heap,val)
        else:
            heapq.heappush(self.min_heap,val)
            self.length += 1
        print(self.min_heap)
        return self.min_heap[0]

            
