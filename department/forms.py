from django.forms import ModelForm
from django import forms
from .models import Department, Course

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

        

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name','department']

        

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        