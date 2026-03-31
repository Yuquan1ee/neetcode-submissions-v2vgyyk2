class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) != 1):
            stones = sorted(stones)
            print(stones)
            if stones[len(stones)-1] == stones[len(stones) - 2]:
                stones.pop()
                stones.pop()
                if len(stones) == 0:
                    return 0

            else:
                new_stones = stones[len(stones)-1] - stones[len(stones)-2]
                stones.pop()
                stones.pop()
                stones.append(new_stones)
        return stones[0]