from datetime import datetime
current_year = datetime.now().year
print(current_year)

class Student:
    def __init__(self, name22, year22, id22):
        self.name = name22
        self.year = year22
        self.id = id22

s1 = Student("Adam",2000, "01234")

print(s1.name, s1.year, s1.id)