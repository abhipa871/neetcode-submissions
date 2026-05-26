class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            list_str = [0]*26
            for character in word:
                list_str[ord('z')-ord(character)]+=1
            groups[tuple(list_str)].append(word)
        return list(groups.values())
