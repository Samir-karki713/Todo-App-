from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'doing_date']  # Add doing_date to the form

    # Specify HTML5 date input type for the doing_date field
    widgets = {
        'doing_date': forms.DateInput(attrs={'type': 'date'}),  # Use the date picker input
    }
