#from attr import fields
from django import forms
from .models import Question, Choice

class TestForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {
            'question_text',
            'pub_date',
        }
