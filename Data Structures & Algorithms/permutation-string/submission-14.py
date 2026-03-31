class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_set = {char: s1.count(char) for char in set(s1)}
        print(s1_set)
        substring = s2[0:len(s1)]
        print(substring)
        s2_set = {char: substring.count(char) for char in set(substring)}
        print(s2_set)
        if s1_set == s2_set:
            return True

        for i in range(len(s1),len(s2)):
            if s2[i] not in s2_set:
                s2_set[s2[i]] = 0
            s2_set[s2[i]] += 1
            s2_set[s2[i-len(s1)]] -= 1
            
            if s2_set[s2[i-len(s1)]] == 0:
                del s2_set[s2[i-len(s1)]]
        
            if s2_set == s1_set:
                return True

        return False