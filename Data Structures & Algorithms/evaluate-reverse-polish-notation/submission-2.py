class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            elif char == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 - n1
                stack.append(res)
            else:
                stack.append(int(char))
            
        return stack[0]