class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            word_char = {}
            for c in s:
                if c not in word_char:
                    word_char[c] = 1
                else:
                    word_char[c] = word_char[c] + 1
            tuple_word_char = tuple(sorted(word_char.items()))
            if tuple_word_char not in answer:
                answer[tuple_word_char] = []
            answer[tuple_word_char].append(s)
       
        return [answer[x] for x in answer ]