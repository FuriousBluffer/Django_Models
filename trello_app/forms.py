from django import forms
from .models import Task, TaskList


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # you could provide a list of files to be displayed here
        fields = '__all__'
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
