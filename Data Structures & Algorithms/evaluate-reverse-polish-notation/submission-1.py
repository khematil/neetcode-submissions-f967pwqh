class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                print(i)
                if tokens[i] in "*-/+":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == "+":
                        result = a + b 
                    elif tokens[i] == "/":
                        result = int(a / b) 
                    elif tokens[i] == "-":
                        result = a - b 
                    elif tokens[i] == "*":
                        result = a * b

                    # omit from values in tokens from [:i-2]
                    # add our result 
                    # and keep tokens from i+1:
                    # print(f"{tokens[i-2]}, {tokens[i-1]}, {tokens[i]}")
                    # print(tokens[:i-2])

                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:] 
                    print(tokens)

                    break
                

        return int(tokens[0])
                                