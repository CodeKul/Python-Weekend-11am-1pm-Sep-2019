class SuperClass:

    def __init__(self, a):
        self.a = a
    
    def display(self):
        print("a:", self.a)


class Sub1(SuperClass):

    def __init__(self, a, a1):
        SuperClass.__init__(self, a)
        self.a1 = a1

    def display(self):
        SuperClass.display(self)
        print('a1:', self.a1)

    def addValue(self, val):
        self.a += val
        self.a1 += val


class Sub2(SuperClass):

    def __init__(self, a, a2):
        SuperClass.__init__(self, a)
        self.a2 = a2

    def display(self):
        SuperClass.display(self)
        print('a2:', self.a2)

    def addValue(self, val):
        self.a += val
        self.a2 += val


def add30(obj):
    obj.addValue(30)


obj1 = Sub1(10, 100)
obj2 = Sub2(20, 200)

obj1.display()
obj2.display()

add30(obj1)
add30(obj2)

obj1.display()
obj2.display()

