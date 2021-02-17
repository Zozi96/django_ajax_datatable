from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'birthday': forms.NumberInput(attrs={'type': 'date'})
        }
