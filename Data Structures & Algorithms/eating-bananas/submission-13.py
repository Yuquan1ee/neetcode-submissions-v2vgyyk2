import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        fast_rate = max(piles)
        slow_rate = 1
        while(slow_rate + 1< fast_rate):
            mid_rate = (fast_rate + slow_rate)//2
            total_time = 0
            for i in piles:
                total_time = total_time + math.ceil(i/mid_rate)
            if total_time >h:
                slow_rate = mid_rate
            elif total_time <=h:
                fast_rate = mid_rate
            

        for i in range(slow_rate, fast_rate + 1):
            print(i)
            total_time = 0
            for x in piles:
                total_time = total_time + math.ceil(x/i)
            print(total_time)
            if total_time <=h:
                return i