# Class Methods

# Notes:

# class methods use 'cls' as their keyword parameter in their brackets
    # - e.g. def class_method(cls)...
        # - similar to how instance methods use 'self'
# - 

# a simple class
class Student:

    # class variable
    student_counter = 0

    # constructor
    def __init__(self, name, exam_title, percentage_score):
        self.name = name
        self.exam_title = exam_title
        self.percentage_score = percentage_score
        Student.student_counter += 1

    # simple instance method
    def student_bio(self):
        return f"Name: {self.name}, Exam Title: {self.exam_title}, Percentage Score: {self.percentage_score}%"
    

    
    
    
# object creation
muffy = Student(name="Muffy", exam_title="Science", percentage_score=78)
arthur = Student(name="Arthur", exam_title="Maths", percentage_score=92)
buster = Student(name="Buster", exam_title="Geography", percentage_score=85)
francine = Student(name="Francine", exam_title="ICT", percentage_score=100)

# printing out objects
print()
print(muffy.student_bio())
print()
print(arthur.student_bio())
print()
print(buster.student_bio())
print()
print(francine.student_bio())
print()
# displays 4 as there has been 4 objects created from the class
print(f"Total number of students: {Student.student_counter}")
print()
print("Congratulations to all! 🥳")
