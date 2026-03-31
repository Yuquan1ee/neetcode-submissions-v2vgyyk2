class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        max_length = 0
        current_length = 0
        previous_index = 0
        for i in range(0, len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = i
                current_length += 1
                
            else:
                print(f"{s[i]} in hash map at index {hash_map[s[i]]}")
                if hash_map[s[i]] > previous_index:
                    previous_index = hash_map[s[i]]
                hash_map[s[i]] = i
                current_length = i - previous_index
                
            if current_length > max_length:
                    max_length = current_length
        return max_length