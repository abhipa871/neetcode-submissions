class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left_ptr = 0
        cache = set()

        for right_ptr in range(len(s)):
            while s[right_ptr] in cache:
                cache.remove(s[left_ptr])
                left_ptr+=1
            cache.add(s[right_ptr])
            max_len = max(max_len, right_ptr-left_ptr +1)
        return max_len
            