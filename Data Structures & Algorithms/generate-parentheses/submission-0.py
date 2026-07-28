class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrace(openN, closeN):
           if openN==closeN==n:
              res.append(''.join(stack))
              return
           if openN<n:
              stack.append('(')
              backtrace(openN+1, closeN)
              stack.pop()
           if closeN<openN:
              stack.append(')')
              backtrace(openN, closeN+1)
              stack.pop()
        backtrace(0,0)
        return res