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
        if re.match(r"\w+", token):
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
    
    return " ".join(postfixList)

print(infixtopostfix("A * B + C * D"))