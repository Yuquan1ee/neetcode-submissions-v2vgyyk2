class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        holding_list = [[temperatures[0],0]]

        for i in range(1,len(temperatures)):
            if temperatures[i] < holding_list[len(holding_list)-1][0]:
                holding_list.append([temperatures[i],i])
            else:
                while(len(holding_list)!=0):
                    if temperatures[i]> holding_list[len(holding_list)-1][0]:
                        results[holding_list[len(holding_list)-1][1]] = i-holding_list[len(holding_list)-1][1]
                        holding_list.pop()
                    else:
                        break
                holding_list.append([temperatures[i],i])


        return results

        