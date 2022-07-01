class Student:
    def __init__(self, name, studentId, gender, age, email):
        self.__name = name
        self.__studentId = studentId
        self.__gender = gender
        self.__age = age
        self.__email = email

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getStudentId(self):
        return self.__studentId

    def setStudentId(self, value):
        self.__studentId = value

    def getGender(self):
        return self.__gender

    def setGender(self, value):
        self.__gender = value

    def getAge(self):
        return self.__age

    def setAge(self, value):
        self.__age = value

    def getEmail(self):
        return self.__email

    def setEmail(self, value):
        self.__email = value
