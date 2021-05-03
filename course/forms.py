from  .models import Course
from django.forms import ModelForm, ValidationError
from django.forms import SelectDateWidget
from django import forms

class CourseForm(ModelForm):
    name = forms.CharField(
        min_length = 7,
        max_length = 30,
        widget = forms.TextInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'Назва курсу'
            }
        )
    )
    description = forms.CharField(
        required = True,
        min_length = 50,
        widget = forms.Textarea(attrs= {
            'class' : 'form-control',
            'placeholder' : 'Опис курсу'
            }
        )
    )
    count = forms.IntegerField(
        min_value = 5,
        widget = forms.NumberInput(attrs= {
            'class' : 'form-control',
            'placeholder' : 'Кількість лекцій'
            }
        )
    )

    end_course = forms.DateTimeField(
        widget=forms.NumberInput(attrs={
            'class' : 'form-control',
            'type': 'date'
            }
        )
    )

    start_course = forms.DateTimeField(
        widget=forms.NumberInput(attrs={
            'class' : 'form-control',
            'type': 'date'
            }
        )
    )
    class  Meta:
        
        model = Course

        fields = ('name', 'description', 'count', 'start_course', 'end_course')

  