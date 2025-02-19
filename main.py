# oop stands for object oriented programmng


class Student:
    # constructor method
    def __init__ (self , name , age , score):
        self.name = name
        self.age = age
        self.score = score
        # Member function
    def display(self):
        print(f"Student name is : {self.name} and my age: {self.age} also my score : {self.score}")
    # instance of the class(object)
myobj=Student(name="Lincoln" ,age=10 , score='C')
myobj.display()
myobj=Student(name="Milly" ,  age=18 , score='A')
myobj.display()
myobj=Student(name="Jelimo" , age=17 , score='D')
myobj.display()
myobj=Student(name="Cheboi" , age=16 , score='O')
myobj.display()
myobj=Student(name="Langat" , age=15 , score='M')
myobj.display()

