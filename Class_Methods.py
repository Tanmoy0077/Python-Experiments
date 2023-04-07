class Student:
    college_name = "MCKVIE"

    def __init__(self, name, std, age) -> None:
        self.name = name
        self.standard = std
        self.age = age

    def getDetails(self):
        return f"The name of the student is {self.name} standard is {self.standard} age is {self.age} and college is {self.college_name}"

    @classmethod
    def change_college(cls, newCollege):
        cls.college_name = newCollege


if __name__ == '__main__':
    st1 = Student("Tanmoy", "B.tech", 19)
    st2 = Student("Yasin", "M.tech", 25)
    print(st1.getDetails())
    """__dict__ prints the instance variables of an object or class variables of a class"""
    # print(Student.__dict__)
    # print(st.__dict__)
    """
    Class method is such a method which can access the class variables and modify them
    Once modified other objects of the class will also get the modified value
    """
    st1.change_college("abc")
    print(st1.getDetails())
    print(st2.getDetails())
