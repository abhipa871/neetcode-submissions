class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)
        for s in strs:
            table = [0] * 26
            for i in s:
                table[ord(i)-ord('a')] = 1 + table[ord(i)-ord('a')]
            hashtable[tuple(table)].append(s)
        return list(hashtable.values())
        