class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        #heapq is a min heap
        heap = [-x for x in stones]
        heapq.heapify(heap)
        print(heap)
        while(len(heap) > 1):
            first_stone = heapq.heappop(heap)
            second_stone = heapq.heappop(heap)
            if first_stone != second_stone:
                heapq.heappush(heap, -abs(first_stone-second_stone))
        return 0 if len(heap) == 0 else -heap[0]