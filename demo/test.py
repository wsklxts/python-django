
import types

class Student:
    def __init__(self,age,name):
        self.age=age
        self.__name=name
    def learn(self):
        print( self.age)


s = Student(12,"六六");


class Student2(Student):
    def __init__(self, name, gender):
        super().__init__(name, gender)

        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.get_gender
    def set_gender(self,name):
        self.get_gender=name

s2 = Student2(123,34)
print(s2.name)
print(setattr(s2,"name","eeeeeeeee"))

print(s2.name)



# type(int)==type(str)==types.TypeType