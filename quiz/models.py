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
    
class Section(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=50)
    def __str__(self):
        return self.section_name

class Difficulty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Objectives(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 
    
class Options(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Option for Q{self.question.id}: {self.option_text}"

class Question(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    question = models.CharField(max_length=600)
    marks = models.PositiveIntegerField(default=4)
    negative_marks = models.IntegerField(default=-1)
    numerical_answer = models.FloatField(blank=True, null=True)
    answer = models.ForeignKey('Options', on_delete=models.CASCADE, blank=True, null=True, related_name='correct_answer')
    difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE)
    objective = models.ForeignKey('Objectives', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_section_id_display()}: {self.question}"
    

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

   