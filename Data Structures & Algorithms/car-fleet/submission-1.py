class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #start from the furthest car -> car position the furthest away.
        position_speed = {position[i]:speed[i] for i in range(0, len(position))}
        print(position_speed)
        position_speed_sorted = list(sorted(position_speed.items()))
        print(position_speed_sorted)
        number_fleet = 1
        timing = (target - position_speed_sorted[-1][0])/position_speed_sorted[-1][1]
        print(timing)
        position_speed_sorted.pop()
        while(len(position_speed_sorted)!= 0):
            x = position_speed_sorted.pop()
            current_timing = (target - x[0])/x[1]
            if current_timing > timing:
                number_fleet += 1

                timing = current_timing

        return number_fleet 
