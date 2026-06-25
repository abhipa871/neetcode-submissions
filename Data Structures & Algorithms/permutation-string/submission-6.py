class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left_ptr, right_ptr = 0,0
        target = [0]*26
        new = [0]*26
        for char in s1: 
            target[ord(char)-ord('a')]+=1
        print(target)
        while right_ptr<len(s2):
            new[ord(s2[right_ptr])-ord('a')]+=1
            while right_ptr-left_ptr+1>len(s1):
                new[ord(s2[left_ptr])-ord('a')]-=1
                left_ptr+=1
            if target==new:
                return True
            right_ptr+=1
        return False