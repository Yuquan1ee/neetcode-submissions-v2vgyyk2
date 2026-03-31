class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for x in strs:
            char = {}
            word_list = list(x)
            for i in word_list:
                if i in char:
                    char[i] = char[i] + 1
                else:
                    char[i] = 1
            char = tuple(sorted(char.items()))
            if char not in anagram_map:
                anagram_map[char] = []
            anagram_map[char].append(x)
        print(anagram_map)
        answer = []
        for i in anagram_map.values():
            answer.append(i)
        return answer
            