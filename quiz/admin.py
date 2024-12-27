from django.contrib import admin

# Register your models here.
from models import Course, Subject, Section, Difficulty, Objectives, Question, Result
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Difficulty)
admin.site.register(Objectives)
admin.site.register(Question)
admin.site.register(Result)