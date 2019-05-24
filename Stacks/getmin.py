
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
    
def getmin(numbers):
    s1 = Stack()
    s2 = Stack()
    for i in numbers.split():
        s1.push(int(i))
    while not s1.isEmpty():
        if s2.isEmpty():
            s2.push(s1.pop())
        poppedElement = s1.pop()
        if poppedElement < s2.peek():
            s2.push(poppedElement)
    return s2.pop()

print(getmin('1 5 2 20 10'))