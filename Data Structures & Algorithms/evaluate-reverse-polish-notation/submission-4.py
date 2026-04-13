class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []

        for i in range(len(tokens)):
            if tokens[i] in "*-+/":
                top = int(tokenStack.pop())
                cumExpr = int(tokenStack.pop())
                if tokens[i] == "+":
                    tokenStack.append(cumExpr+top) 
                elif tokens[i] == "/":
                    tokenStack.append(int(cumExpr / top)) 
                elif tokens[i] == "-":
                    tokenStack.append(cumExpr - top)
                elif tokens[i] == "*":
                    tokenStack.append(cumExpr * top)
            else:
                tokenStack.append(tokens[i])
        
        print(tokenStack)

        return int(tokenStack[-1])
