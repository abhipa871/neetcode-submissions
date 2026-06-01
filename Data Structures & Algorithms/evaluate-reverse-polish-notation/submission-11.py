import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            elif len(stack)>1:
                print(stack)
                op2 = stack.pop()
                op1 = stack.pop()
                result = ops[token](op1, op2)
                stack.append(int(result))
        print(stack)
        return stack[-1]