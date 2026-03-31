class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        dict_freq = {}
        for i in range(0, len(nums)):
            if nums[i] not in dict_num:
                dict_num[nums[i]] = 1
                if 1 not in dict_freq:
                    dict_freq[1] = set()
                dict_freq[1].add(nums[i])
            
            else:
                freq = dict_num[nums[i]]
                dict_num[nums[i]] = dict_num[nums[i]] + 1
                dict_freq[freq].remove(nums[i])
                if (freq + 1) not in dict_freq:
                    dict_freq[freq + 1] = set()
                dict_freq[freq + 1].add(nums[i])
        remain = k
        nums = []
        while (remain !=0):
            high_freq = max(dict_freq)
            remain = remain - len(dict_freq[high_freq])
            for i in dict_freq[high_freq]:
                nums.append(i)
            dict_freq.pop(max(dict_freq))
        return nums
