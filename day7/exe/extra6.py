class Student:
    school_name = "Default High School"

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def average_grade(self):
        
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def student_info(self):
       
        avg = self.average_grade()
        return (f"Student: {self.name}, School: {Student.school_name}, "
                f"Average Grade: {avg:.2f}")


student1 = Student("Taha")
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2 = Student("FAWAZ")
student2.add_grade(101)  
student2.add_grade(88)

print(student1.student_info())
print(student2.student_info())
