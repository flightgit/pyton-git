from datetime import datetime


class Student:
    def __init__(self, name2, year2, id2):
        self.name = name2
        self.year = year2
        self.id = id2

def c_age(self):
    currnet_year = datetime.now().year
    return currnet_year - self.year


s1 = Student("Adam", 2000, "012345678")

age = s1.c_age()
print(age)