class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        set_s = {}
        set_t = {}
        if len(list_s) != len(list_t):
            return False

        for i in range(0,len(list_s)):
            if list_s[i] not in set_s:
                set_s[list_s[i]] = 1
            else:
                set_s[list_s[i]] = set_s[list_s[i]] + 1

            if list_t[i] not in set_t:
                set_t[list_t[i]] = 1
            else:
                set_t[list_t[i]] = set_t[list_t[i]] + 1
        
        if set_s == set_t:
            return True
        else:
            return False
        