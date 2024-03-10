class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.grades = (88,99, 77, 76)
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    
student = Student("Jim")
print(f"Student {student.name} average is: ", student.average())