class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        '''
        Given array of strings tokens in reverse polish notation
        return integer that represents value of the expression
        '''
        stack = []
        for c in tokens:
            # performs math operation and reappends new value to stack
            if c == "+":
                stack.append(stack.pop() + stack.pop())
                
            elif c == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif c == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(int(num1 / num2))
            
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            else:
                stack.append(int(c))
        
        return int(stack[-1])
        
        
        

solution = Solution()
# tokens = ["2","1","+","3","*"] #9
# tokens = ["4","13","5","/","+"] #6
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #22
print(solution.evalRPN(tokens))
