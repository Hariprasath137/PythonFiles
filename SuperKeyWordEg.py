"""class a():
    def __init__(self):
        print("A")
    def display(self):
        print("This is A class")

class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("This is B Class")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("This is C Class")

obj = c()"""

class Grandpa():
    def __init__(self):
        print("Grandpa's Asset")

class Father():
    def __init__(self):
        super().__init__()
        print("Father's Money")

class Son(Father,Grandpa):
    def __init__(self):
        super().__init__()
        print("Son Enjoying")


value = Son();


