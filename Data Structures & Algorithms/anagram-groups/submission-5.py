class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for s in strs:
            count = [0] * 26
            print(count)
            for c in s:
                count[ord(c)-ord("a")] +=1
            tuple_count = tuple(count)
            answer[tuple_count].append(s)

        return [answer[x] for x in answer]