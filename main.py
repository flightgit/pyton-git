from datetime import datetime


class Student:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def c_age(self):
        current_year = datetime.now().year
        return current_year - self.year


s1 = Student("Adam", 2000, "012345678")
s2 = Student("Yossi", 2005, "876543210")
s3 = Student("Dan", 1974, "343985671")

age = s1.c_age()
print(age)
age = s2.c_age()
print(age)
age = s1.c_age()
print(age)