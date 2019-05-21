class Fraction:
    def __init__(self,top,bottom):
        self.Num = top
        self.Den = bottom
        common = gcd(self.Num, self.Den)
        self.Num = self.Num // common
        self.Den = self.Den // common

    def __add__(self, otherfraction):
        newNum = self.Num*otherfraction.Den + self.Den*otherfraction.Num
        newDen = self.Den*otherfraction.Den
        return Fraction(newNum, newDen)

    def __sub__(self , otherfraction):
        newNum = self.Num*otherfraction.Den - self.Den*otherfraction.Num
        newDen = self.Den*otherfraction.Den
        return Fraction(newNum, newDen)

    def __mul__(self , otherfraction):
        newNum = self.Num*otherfraction.Num
        newDen = self.Den*otherfraction.Den
        return Fraction(newNum , newDen)
    
    def __truediv__(self , otherfraction):
        newNum = self.Num*otherfraction.Den
        newDen = self.Den*otherfraction.Num
        return Fraction(newNum, newDen)

    def __gt__(self , otherfraction):
        Num1 = self.Num*otherfraction.Den
        Num2 = self.Den*otherfraction.Num
        return Num1 > Num2

    def __ge__(self, otherfraction):
        Num1 = self.Num*otherfraction.Den
        Num2 = self.Den*otherfraction.Num
        return Num1 >= Num2

    def __lt__(self, otherfraction):
        Num1 = self.Num*otherfraction.Den
        Num2 = self.Den*otherfraction.Den
        return Num1 < Num2

    def __le__(self, otherfraction):
        Num1 = self.Num*otherfraction.Den
        Num2 = self.Den*otherfraction.Den
        return Num1 <= Num2

    def __ne__(self, otherfraction):
        Num1 = self.Num*otherfraction.Den
        Num2 = self.Den*otherfraction.Den
        return Num1 != Num2
    

    def getNum(self):
        return self.Num
    def getDen(self):
        return self.Den
    def __str__(self):
        return str(self.Num) + "/" + str(self.Den)

def gcd(a , b):
        while a%b!=0:
            a, b = b, a%b
        return b    

def main():
    f1 = Fraction(2,4)
    f2 = Fraction(3,5)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = f1 * f2
    # f6 = f1 / f2
    print("{}+{}={}".format(f1,f2,f3))
    print("{}-{}={}".format(f1,f2,f4))
    print("{}*{}={}".format(f1,f2,f5))
    # print("{}//{}={}".format(f1,f2,f6))
    print("{}>{}= {}".format(f1,f2,f1>f2))
    print("{}<{}= {}".format(f1,f2,f1<f2))
    print("{}>={}= {}".format(f1,f2,f1>=f2))
    print("{}<={}= {}".format(f1,f2,f1<=f2))
    print("{}!={}={}".format(f1,f2,f1!=f2))

main()