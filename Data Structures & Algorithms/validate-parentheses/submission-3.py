class Solution:
    def isValid(self, s: str) -> bool:
        open_brac = {"(", "[", "{"}
        brac_pair = {")":"(", "]":"[", "}":"{"}
        holding_list = []
        for i in s:
            if i in open_brac:
                holding_list.append(i)
            else: # closed brac
                try:
                    last = holding_list.pop()
                    if last != brac_pair[i]:
                        return False

                except:
                    return False

        if len(holding_list) == 0:
            return True
        else:
            return False