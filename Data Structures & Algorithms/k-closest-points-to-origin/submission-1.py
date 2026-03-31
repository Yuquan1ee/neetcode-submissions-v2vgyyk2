from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = [] # max heap
        counter = 0
        for x in points:
            
            distance = -1 * sqrt((x[0])**2 + (x[1])**2)
            
            if len(answer) == 0:
                answer.append((distance,(x[0],x[1])))
                heapq.heapify(answer)
                counter +=1
            elif counter < k:
                heapq.heappush(answer, (distance,(x[0],x[1])))
                counter += 1
            else:
                if distance < answer[0][0]:
                    continue
                else:
                    heapq.heappushpop(answer,(distance,(x[0],x[1])))
        final = []
        for x in answer:
            final.append([x[1][0], x[1][1]])
        return final                    
                    