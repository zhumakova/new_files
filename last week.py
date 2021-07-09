class Student:
    student_count=0

    def __init__(self,name:int,specialization:int):
        self.name=name
        self.specialization=specialization
        Student.student_count+=1
        self.id = Student.student_count
s1=Student('cholpon','manger')
s2=Student('begimai','DS')
print()


