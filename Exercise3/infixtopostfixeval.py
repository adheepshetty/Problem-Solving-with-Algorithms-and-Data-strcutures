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
    
    

def infixtopostfix(infixexpr):
    prec = {}
    prec["*"] = prec["/"] = 3
    prec["+"] = prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if re.match(r"\d+", token):
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()]) >= (prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return postfixList

def infixtopostfixeval(infixexpr):
    operandStack = Stack()
    tokenlist = infixtopostfix(infixexpr)

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

print(infixtopostfixeval('( 7 + 8 ) / ( 3 + 2 )'))