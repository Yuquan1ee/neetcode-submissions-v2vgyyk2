class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        list_freq = [[]for i in range(len(nums) + 1)]

        for n in nums:
            dict_num[n] = 1 + dict_num.get(n,0)
        for x,y in dict_num.items():
            list_freq[y].append(x)

        res = []
        print(list_freq)

        for i in range(len(list_freq) - 1, 0, -1):
            for n in list_freq[i]:
                print(n)
                res.append(n)
                if len(res) == k:
                    return res
        
