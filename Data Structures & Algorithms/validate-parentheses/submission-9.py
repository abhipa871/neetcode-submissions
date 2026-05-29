class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        hashmap = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char not in hashmap:
                op.append(char)
            elif char in hashmap:
                if len(op)>0 and hashmap[char] == op[-1]:
                    op.pop()
                else:
                    return False
        return len(op) == 0
