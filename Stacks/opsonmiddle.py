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
    def findmiddle(self):
        return (self.items[((len(self.items)-1)//2)-1] if len(self.items)//2 == 0 else self.items[(len(self.items)-1)//2])
    def deletemiddle(self):
        middleelement  = (self.items[((len(self.items)-1)//2)-1] if len(self.items)//2 == 0 else self.items[(len(self.items)-1)//2])
        self.items.remove(middleelement)
        
    
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(40)
s1.push(30)
print(s1.findmiddle())
s1.deletemiddle()
print(s1.items)