class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        self.__salary = new_salary



teacher1 =Teacher( "John Doe",  35, 50000)
print("Teacher's name:", teacher1.name)
print("Teacher's age:", teacher1.age)

print("Teacher's salary:", teacher1.get_salary())


teacher1.set_salary(input('enter the teacher1.set_salary:'))
print("Updated salary:", teacher1.get_salary())