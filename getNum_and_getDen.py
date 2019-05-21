class Fraction:
    def __init__(self,top,bottom):
        self.Num = top
        self.Den = bottom
    def getNum(self):
        return self.Num
    def getDen(self):
        return self.Den
    def __str__(self):
        return str(self.Num) + "/" + str(self.Den)
myfraction = Fraction(3,5)
print(myfraction.getNum())
print(myfraction.getDen())
print(myfraction)

