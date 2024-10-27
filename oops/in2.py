#Multiple inheritance
class A:
    def __init__(self):
        print('Class A')

    def sum(self,a,b):
        print('Sum=', a+b)

class B:
    def __init__(self):
        print('Class B')

    def diff(self,a,b):
        print('Diff=', a-b)

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('Class Child')

ob1 = C()
ob1.sum(10,20)
ob1.diff(100,30)