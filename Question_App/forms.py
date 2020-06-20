from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer']
        widgets = {
          'answer': forms.Textarea(attrs={'rows':3, 'cols':25}),
        }
