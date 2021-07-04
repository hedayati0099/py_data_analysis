class human:
    count = 0

    def __init__(self, name, age, number,gender):
        self.name = name
        self.age = age
        self.num = number
        self.gen = gender 
        human.count += 1

    def __str__(self):
        return f"{self.name}'s number is {self.num}"


class Employee(human):
    def hughugh(self, salary):
        self.salary = salary
    
    def __str__(self):
        return f"{self.name}'s number is {self.num} and he/she salary is {self.salary} "

# next line classes are all just for example now 
# for now we don't work on them

class programmer(Employee):
    pass                                                

class monshi(Employee):
    pass

class moshaver(Employee):
    pass

class hesabdar(Employee):
    pass
class boss(Employee):
    pass

name = ['reza','sara','hoda','ali','amir','javad','parsa','zahra']
age = [33,44,19,23,27,29,34,50]
number = [334,222,444,221,554,666,445,777]
gender = ['m','f','f','m','m','m','m','f']
salary = [6,7,4,4,5,9,9,20]

for i in range(8):
    a = Employee(name[i],age[i],number[i],gender[i])
    a.salary = salary[i]
    print(a)

print(human.count)


# you may have 8 people's info in your output
