from django.db import models

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name
   
class Subject(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    subject_name=models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name
    
    #we dont want sections
    
# class Section(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return f"{self.course.name} - {self.name}"

class Question(models.Model):
    SECTION_ID_CHOICES = [
        ('MCQ', 'Multiple Choice Question'),
        ('NUM', 'Numerical'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    OBJECTIVE_TYPE_CHOICES = [
        ('remember', 'Remember'),
        ('understand', 'Understand'),
        ('apply', 'Apply'),
        ('analyse', 'Analyse'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=4)
    negative_marks = models.IntegerField(default=-1)
    question = models.CharField(max_length=600)
    section_id = models.CharField(max_length=3, choices=SECTION_ID_CHOICES, default='MCQ')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    objective = models.CharField(max_length=10, choices=OBJECTIVE_TYPE_CHOICES, default='remember')

    # For MCQ-specific questions
    option1 = models.CharField(max_length=200, blank=True, null=True)
    option2 = models.CharField(max_length=200, blank=True, null=True)
    option3 = models.CharField(max_length=200, blank=True, null=True)
    option4 = models.CharField(max_length=200, blank=True, null=True)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat, blank=True, null=True)

    # For Numerical questions
    numerical_answer = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_section_id_display()}: {self.question}"
    
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

