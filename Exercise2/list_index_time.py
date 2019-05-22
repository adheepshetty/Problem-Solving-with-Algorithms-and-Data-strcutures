from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

def test5():
    l = [2,1,2,3]
    return l.index(1)

t1 = Timer("test1()", "from __main__ import test1")
print("Concat: {} milliseconds".format(t1.timeit(number = 1000)))

t2 = Timer("test2()", "from __main__ import test2")
print("Append: {} milliseconds".format(t2.timeit(number = 1000)))

t3 = Timer("test3()", "from __main__ import test3")
print("Comprehension: {} milliseconds".format(t3.timeit(number = 1000)))

t4 = Timer("test4()", "from __main__ import test4")
print("List Range: {} milliseconds".format(t4.timeit(number = 1000)))

t5 = Timer("test5()","from __main__ import test5")
print("Index: {} milliseconds".format(t5.timeit(number=1000)))