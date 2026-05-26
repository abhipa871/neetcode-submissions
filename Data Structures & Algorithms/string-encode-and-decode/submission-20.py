class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''.join(f'{len(s)}#{s}' for s in strs)
        return string
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1

            length = int(s[i:j])      # number before #
            i = j + 1                 # skip '#'
            res.append(s[i:i+length]) # take word
            i += length               # move to next chunk

        return res