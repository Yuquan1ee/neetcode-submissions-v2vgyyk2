import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(string)
        string = string.lower()
        string_list = list(string)
        for i in range(0, len(string_list)):
            if string_list[i] == string_list[len(string_list)-i-1]:
                continue
            else:
                return False
        return True