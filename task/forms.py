
from django import forms
from django.forms import ModelForm
from .models import task_model

class TaskForm(ModelForm) :
    task = forms.CharField( label='' , widget=forms.TextInput(attrs={"placeholder": "Write your topic "})) 


    class Meta:
        model = task_model
        fields = [
            'task' ,
        ]


