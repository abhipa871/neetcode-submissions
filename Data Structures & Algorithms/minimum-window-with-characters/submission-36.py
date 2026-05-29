from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t

        left_ptr = 0
        count_t = defaultdict(int)
        count_s = defaultdict(int)

        freq = 0
        res = [-1, -1]
        min_len = float("inf")

        for ch in t:
            count_t[ch] += 1

        for right_ptr in range(len(s)):
            right_char = s[right_ptr]
            count_s[right_char] += 1

            if right_char in count_t and count_s[right_char] == count_t[right_char]:
                freq += 1

            while freq == len(count_t):
                if right_ptr - left_ptr + 1 < min_len:
                    res = [left_ptr, right_ptr]
                    min_len = right_ptr - left_ptr + 1

                left_char = s[left_ptr]
                count_s[left_char] -= 1

                if left_char in count_t and count_s[left_char] < count_t[left_char]:
                    freq -= 1

                left_ptr += 1

        l, r = res
        return s[l:r + 1] if min_len != float("inf") else ""