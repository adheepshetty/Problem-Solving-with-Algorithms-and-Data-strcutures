import re
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == [] 
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def postfixeval(postfixexpr):
    operandStack = Stack()
    tokenlist = postfixexpr.split()

    for token in tokenlist:
        if re.match(r"\d+", token):
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = domath(token, int(operand1), int(operand2))
            operandStack.push(result)
    return operandStack.pop()

def domath(token , operand1, operand2):
    if token  == "+":
        return operand1 + operand2
    elif token == "-":
        return operand1 - operand2
    elif token  == "*":
        return operand1 * operand2
    else:
        return operand1 / operand2
    
print(postfixeval('7 8 + 3 2 + /'))