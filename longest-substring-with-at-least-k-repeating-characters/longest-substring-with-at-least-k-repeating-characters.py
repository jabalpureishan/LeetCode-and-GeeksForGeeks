class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0    
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        all_chars_meet_requirement = all(count >= k for count in char_count.values())
        if all_chars_meet_requirement:
            return len(s)
        start, result = 0, 0
        for i, char in enumerate(s):
            if char_count[char] < k:
                result = max(result, self.longestSubstring(s[start:i], k))
                start = i + 1
        result = max(result, self.longestSubstring(s[start:], k))
        return result

             
