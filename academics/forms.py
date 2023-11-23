from django.forms import ModelForm
from django import forms
from .models import AcademicDetails,Units, RegisterUnits

class AcademicDetailsForm(ModelForm):
    class Meta:
        model = AcademicDetails
        fields = ['student', 'course']

        

    def __init__(self, *args, **kwargs):
        super(AcademicDetailsForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class UnitsForm(ModelForm):
    class Meta:
        model = Units
        fields = ['unit_name', 'unit_code', 'course']

        

    def __init__(self, *args, **kwargs):
        super(UnitsForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class RegisterUnitsForm(ModelForm):
    class Meta:
        model = RegisterUnits
        fields = ['unit_id',]

        

    def __init__(self, *args, **kwargs):
        super(RegisterUnitsForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
