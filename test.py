from Student import Student
from Person import Person

# instantiate an object of the class Student
student = Student("Mike", "123456", "M", 18, "email.com")
print(student.getName())

student.setName("John")
print(student.getName())


# instantiate an object of the class People
person = Person("Lily", "123456", "F", 20, "email.com")
person.name = "Niki"
print(person.name)

# get private attribute
# print(student._Student__name)
