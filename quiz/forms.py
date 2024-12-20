from django import forms
from . import models
from django.core.exceptions import ValidationError
from .models import Question, Course, Section, Difficulty, Subject, Objectives

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary = forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['course_name', 'question_number', 'total_marks']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = ['subject_name']

class QuestionForm(forms.ModelForm):
    courseID = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Select Course",
        to_field_name="id"
    )
    subjectID = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        empty_label="Select Subject",
        to_field_name="id"
    )
    sectionID = forms.ModelChoiceField(
        queryset=Section.objects.all(),
        empty_label="Select Section",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name="id"
    )
    difficultyID = forms.ModelChoiceField(
        queryset=Difficulty.objects.all(),
        empty_label="Select Difficulty"
    )
    objectiveID = forms.ModelChoiceField(
        queryset=Objectives.objects.all(),
        empty_label="Select Objective"
    )

    # Only show these fields if the section is MCQ
    option1 = forms.CharField(max_length=255, required=False, label='Option 1')
    option2 = forms.CharField(max_length=255, required=False, label='Option 2')
    option3 = forms.CharField(max_length=255, required=False, label='Option 3')
    option4 = forms.CharField(max_length=255, required=False, label='Option 4')

    # Correct answer field (select from the options)
    correct_option = forms.ChoiceField(
        choices=[('Option 1', 'Option 1'), 
                 ('Option 2', 'Option 2'), 
                 ('Option 3', 'Option 3'), 
                 ('Option 4', 'Option 4')],
        required=False,
        label="Correct Answer"
    )

    # Numerical answer field (only for numerical questions)
    numerical_answer = forms.FloatField(required=False, label="Numerical Answer")

    class Meta:
        model = Question
        fields = [
            'courseID', 'sectionID', 'subjectID','question','difficultyID', 'objectiveID', 
            'numerical_answer', 'correct_option', 
            'option1', 'option2', 'option3', 'option4'
        ]
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

    def clean(self):
        cleaned_data = super().clean()
        section = cleaned_data.get("sectionID")

        # Ensure the numerical_answer field is used only for "NUM" sections
        if section and section.section_name == "NUM" and any([cleaned_data.get(f"option{i}") for i in range(1, 5)]):
            raise forms.ValidationError("Options should not be provided for Numerical questions.")

        # Ensure the options and correct answer are required only for "MCQ" questions
        if section and section.section_name == "MCQ":
            if not cleaned_data.get("answer"):
                raise forms.ValidationError("Correct answer is required for MCQ questions.")
            if not any([cleaned_data.get(f"option{i}") for i in range(1, 5)]):
                raise forms.ValidationError("At least one option is required for MCQ questions.")

        return cleaned_data

