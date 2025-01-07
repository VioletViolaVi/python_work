# Class Methods

# Notes:

# class methods use 'cls' as their keyword parameter in their brackets
    # - e.g. def class_method(cls)...
        # - similar to how instance methods use 'self'


# a simple class
class Student:

    # class variables
    student_counter = 0
    total_percentage_score = 0
    average_percentage_score = 0

    # constructor
    def __init__(self, name, exam_title, percentage_score):
        self.name = name
        self.exam_title = exam_title
        self.percentage_score = percentage_score
        Student.student_counter += 1
        Student.total_percentage_score += percentage_score
        # average -> addition of all numbers then divide by number of numbers
        # calculates average percentage score of all students
        Student.average_percentage_score = Student.total_percentage_score / Student.student_counter

    # simple instance method
        # - 'self' is used in brackets
    def student_bio(self):
        
        # string has been formatted to make text appear clearer to read
        return f"Name: {self.name:<10} Exam Title: {self.exam_title:<10} Percentage Score (%): {self.percentage_score:<10}"
    
    # class method
        # - 'cls' is used in brackets
            # - 'cls' means class
    # '@classmethod' decorator to be added whenever a class method is to be made
    # this '@classmethod' is used to get the value of the class variable & use it in the f string
    @classmethod
    def student_total(cls):

        # class variable to gotten via dot notation using 'cls' parameter/keyword
            # - DO NOT use class name to get class variable when inside a '@classmethod'
                # - i.e.: NO!!! ----- {Class_name.class_variable} ----- NO!!!
        return f"Total number of students so far: {cls.student_counter}"
    
    # gets average percentage score of all students
    @classmethod
    def average_score(cls):
        return f"The average score of all the students(%): {cls.average_percentage_score}"
    
    
# object creation
muffy = Student(name="Muffy", exam_title="Science", percentage_score=78)

# shows how many objects from 'Student' class has been made up to this point
print(Student.student_total())

arthur = Student(name="Arthur", exam_title="Maths", percentage_score=92)

# shows how many objects from 'Student' class has been made up to this point
print(Student.student_total())

buster = Student(name="Buster", exam_title="Geography", percentage_score=85)

# shows how many objects from 'Student' class has been made up to this point
print(Student.student_total())

francine = Student(name="Francine", exam_title="ICT", percentage_score=100)

# shows how many objects from 'Student' class has been made up to this point
# displays 4 as there has been 4 objects created from the class
print(Student.student_total())

print()
# printing out objects from 'Student' class
print(muffy.student_bio())
print(arthur.student_bio())
print(buster.student_bio())
print(francine.student_bio())
print()
# prints out average score from class method above
print(Student.average_score())
print()
print("Congratulations to all! 🥳")
