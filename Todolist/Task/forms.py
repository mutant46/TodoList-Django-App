from django import forms
from .models import Task
from django.conf import settings

class TaskcreationForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields  = ('name', 'description', )


class TaskEditForm(forms.ModelForm):
    Completion_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(attrs={
        'placeholder' : 'DD-MM-YYYY',
    }))
    class Meta:
        model = Task
        fields  = ('name', 'description', 'Completion_date')
