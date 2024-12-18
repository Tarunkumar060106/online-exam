from django import forms
from . import models
from django.core.exceptions import ValidationError
from .models import Options, Section

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
        queryset=models.Course.objects.all(),
        empty_label="Select Course",
        to_field_name="id"
    )
    sectionID = forms.ModelChoiceField(
        queryset=models.Section.objects.all(),
        empty_label="Select Section",
        to_field_name="id"
    )
    difficultyID = forms.ModelChoiceField(
        queryset=models.Difficulty.objects.all(),
        empty_label="Select Difficulty"
    )
    objectiveID = forms.ModelChoiceField(
        queryset=models.Objectives.objects.all(),
        empty_label="Select Objective"
    )

    # Fields for the MCQ options
    option1 = forms.ModelChoiceField(queryset=Options.objects.all(), required=False, label='Option 1')
    option2 = forms.ModelChoiceField(queryset=Options.objects.all(), required=False, label='Option 2')
    option3 = forms.ModelChoiceField(queryset=Options.objects.all(), required=False, label='Option 3')
    option4 = forms.ModelChoiceField(queryset=Options.objects.all(), required=False, label='Option 4')

    # Numerical answer field
    numerical_answer = forms.FloatField(required=False, label='Numerical Answer')

    # Answer field for MCQs (Selecting the correct option)
    answer = forms.ModelChoiceField(
        queryset=Options.objects.all(), 
        empty_label="Select Correct Answer", 
        required=False
    )

    class Meta:
        model = models.Question
        fields = ['courseID', 'sectionID', 'question', 'marks', 'negative_marks', 'difficultyID', 'objectiveID', 'numerical_answer', 'answer', 'option1', 'option2', 'option3', 'option4']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

def clean(self):
        cleaned_data = super().clean()
        section_id = cleaned_data.get("sectionID")

        # Validate for MCQs
        if section_id:
            section = Section.objects.get(id=section_id)  # Ensure Section is also imported
            if section.section_name == "MCQ":
                if not any([cleaned_data.get("option1"), cleaned_data.get("option2"), cleaned_data.get("option3"), cleaned_data.get("option4")]):
                    raise forms.ValidationError("MCQ questions must have at least one option.")
                answer = cleaned_data.get("answer")
                if not answer:
                    raise forms.ValidationError("MCQ questions must have a correct answer selected.")
                # Ensure the answer is one of the options
                valid_answers = [cleaned_data.get("option1"), cleaned_data.get("option2"), cleaned_data.get("option3"), cleaned_data.get("option4")]
                if answer not in valid_answers:
                    raise forms.ValidationError("The selected correct answer must be one of the provided options.")
    
        return cleaned_data