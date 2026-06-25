class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        window = defaultdict(int)
        min_string = ""
        min_len = float('inf')
        for char in t:
            target[char]+=1
        have = 0
        need = len(target)
        left_ptr, right_ptr = 0,0
        while right_ptr<len(s):
          ch = s[right_ptr]
          window[ch]+=1
          if ch in target and window[ch]==target[ch]:
            have+=1
          while have==need:
             if len(s[left_ptr:right_ptr+1])<min_len:
                min_string = s[left_ptr:right_ptr+1]
                min_len = len(s[left_ptr:right_ptr+1])
             window[s[left_ptr]]-=1
             if s[left_ptr] in target and window[s[left_ptr]]<target[s[left_ptr]]:
                have-=1
             left_ptr+=1
          
          right_ptr+=1
        return min_string