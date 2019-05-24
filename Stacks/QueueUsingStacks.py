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

def queueusingstack(numbers):
    s1 = Stack()
    s2 = Stack()
    for i in numbers.split():
        s1.push(int(i))
    while not s1.isEmpty():
        s2.push(s1.pop())
    while not s2.isEmpty():
        print(s2.pop())
    
    
queueusingstack('1 2 3 4 5 6')
    
    