class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left_ptr = 0
        s1_arr = [0]*26
        s2_arr = [0]*26
        for i in range(len(s1)):
            s1_arr[ord(s1[i])-ord('a')]+=1
        for right_ptr in range(len(s2)):
            s2_arr[ord(s2[right_ptr])-ord('a')]+=1
            while right_ptr-left_ptr+1 > len(s1):
                s2_arr[ord(s2[left_ptr])-ord('a')]-=1
                left_ptr+=1
            if s1_arr == s2_arr:
                return True
        return False