class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":  # scan forward until we hit #
                j += 1
            cur_length = int(s[i:j])  # extract full number between i and #
            word = s[j+1:j+1+cur_length]
            res.append(word)
            i = j + 1 + cur_length
        return res
