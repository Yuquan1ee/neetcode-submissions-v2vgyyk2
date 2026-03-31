class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_set = {char: s1.count(char) for char in set(s1)}
        print(s1_set)
        s2_set = {}
        s2_holding = []
        for i in range(0, len(s1)):
            if s2[i] not in s2_set:
                s2_set[s2[i]] = 0
            s2_set[s2[i]] += 1
            s2_holding.append(s2[i])
        k = len(s1)
        if s2_set == s1_set:
            return True
        while(k<len(s2)):
            popped_char = s2_holding.pop(0)
            s2_set[popped_char] -= 1
            if s2_set[popped_char] == 0:
                del s2_set[popped_char]
            s2_holding.append(s2[k])
            if s2[k] not in s2_set:
                s2_set[s2[k]] = 0
            s2_set[s2[k]] += 1
            if s2_set == s1_set:
                return True
            k += 1
        return False