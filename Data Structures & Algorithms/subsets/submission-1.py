class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # quantity of solution is 2**nums
        answer = [[]]
        for i in nums:
            for x in range(len(answer)):
                cur = answer[x].copy()
                print(cur)
                cur.append(i)
                answer.append(cur)
        return answer
            



        






        
    