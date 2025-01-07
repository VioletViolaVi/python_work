# Class Methods

# Notes:

# class methods use 'cls' as their keyword parameter in their brackets
    # - e.g. def class_method(cls)...
        # - similar to how instance methods use 'self'
# - 

# a simple class
class Student:

    # constructor
    def __init__(self, name, exam_title, percentage_score):
        self.name = name
        self.exam_title = exam_title
        self.percentage_score = percentage_score

    # simple instance method
    def student_bio(self):
        return f"Name: {self.name}, Exam Title: {self.exam_title}, Percentage Score: {self.percentage_score}%"
