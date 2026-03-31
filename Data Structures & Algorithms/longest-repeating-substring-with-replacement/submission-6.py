class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 1
        holding_list = [s[0]]
        char_freq = {s[0]:1}
        max_char = s[0]
        for i in range(1, len(s)):
            holding_list.append(s[i])
            if s[i] not in char_freq:
                char_freq[s[i]] = 0
            char_freq[s[i]] += 1
            
                
            if s[i] != max_char: # not equal to current_max
                if char_freq[s[i]]> char_freq[max_char]:
                    max_char = s[i]
                
                while(len(holding_list) - char_freq[max_char]>k):
                    popped_item = holding_list.pop(0)
                    char_freq[popped_item] -= 1
                    max_char = max(char_freq, key=char_freq.get)
               
            if (len(holding_list)>max_length):
                max_length = len(holding_list)
            print(holding_list)
        return max_length
