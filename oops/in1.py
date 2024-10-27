#Single Level
class A:
    def __init__(self):
        print('Base Class')

    def sum(self, a, b):
        print('Sum =', (a+b))

class B(A):
    def __init__(self):
        A.__init__(self)
        print('Class Child')

# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         print('Class Child')

ob1 = B()
ob1.sum(10,20)