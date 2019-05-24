class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def StacksUsingQueues(numbers):
    q1 = Queue()
    q2 = Queue()
    for i in numbers.split()[:-1]:
        q1.enqueue(i)
    q2.enqueue(numbers.split()[-1])
    count = 0
    while count < q1.size()-1:
        removedElement = q1.dequeue()
        q1.enqueue(removedElement)
        count +=1
    while not q1.isEmpty():
        q2.enqueue(q1.dequeue())
    while not q2.isEmpty():
        print(q2.dequeue())

StacksUsingQueues('10 20 30 40')