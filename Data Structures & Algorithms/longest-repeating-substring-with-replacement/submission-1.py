class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_ptr = 0
        maxf = 0
        max_len = 0
        count = defaultdict(int)
        for right_ptr in range(len(s)):
            count[s[right_ptr]]+=1
            maxf = max(maxf, count[s[right_ptr]])
            while (right_ptr-left_ptr+1)-maxf > k:
                count[s[left_ptr]]-=1
                left_ptr+=1
            max_len = max(max_len, right_ptr-left_ptr+1)
        return max_len


            