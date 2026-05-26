class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for string in strs:
            arr = [0]*26
            for char in string:
                arr[ord(char)-ord('a')]+=1
            words.setdefault(tuple(arr), []).append(string)
        return list(words.values())