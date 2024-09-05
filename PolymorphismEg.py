
"""
class animal():
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def __init__(self):
        super().__init__()     #super key word
        print("dog barks")

class bird(animal):
    def sound(self):           #polymorphism
        print("Birds sings")


b = bird()
b.sound()
    


"""

"""class Shape():
    def area():
        return 0

class Rectangle(Shape):
    def area(self):
        l=7
        w=3
        print(l*w)

R1 = Rectangle()


R1.area()
print(R1.area)"""


"""
class person():
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
    def display(self):
        print(self.name,self.grade)

        

s1 = student("harish","E")

s1.display()

"""

"""
class vehicle():
    def start(self):
        print("Vehicle Started")

class car(vehicle):
    def start(self):
        print("Car Started")

c1 = car()

c1.start()

"""

class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def display(self):
        print(self.name,self.salary,self.department)

m1 = manager("Hari","25000","Biomedical")

m1.display()    








































