from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name','question_number','total_marks']

class SubjectForm(forms.ModelForm):
    class Meta:
        model=models.Subject
        fields=['subject_name']

class QuestionForm(forms.ModelForm):
    
    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Course Name", to_field_name="id")
    subjectID=forms.ModelChoiceField(queryset=models.Subject.objects.all(),empty_label="Subject Name", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['question','option1','option2','option3','option4','answer','numerical_answer','section_id','difficulty','objective']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

    def clean(self):
        cleaned_data = super().clean()
        section_id = cleaned_data.get("section_id")

        if section_id == "MCQ":
            if not cleaned_data.get("option1") or not cleaned_data.get("answer"):
                raise forms.ValidationError("MCQ questions must have options and a correct answer.")
        elif section_id == "NUM":
            if cleaned_data.get("numerical_answer") is None:
                raise forms.ValidationError("Numerical questions must have a numerical answer.")
        return cleaned_data