class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {s[0]:1}
        max_length = 1
        max_char = s[0]

        for i in range(1, len(s)):
            
            if s[i] not in char_map:
                char_map[s[i]] =  0
            char_map[s[i]] += 1
            # update the max_char first
            if char_map[s[i]]>char_map[max_char]:
                max_char = s[i]

            if max_length + 1 - char_map[max_char] <= k: #valid window
                max_length = max_length + 1
            else:
                char_map[s[i-max_length]] -=1
                max_char = max(char_map, key=char_map.get)
            print(s[i], char_map)

        return max_length

            
            # when we found up to a specific substring size, we should not reduce the substring