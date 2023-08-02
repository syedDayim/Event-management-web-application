from django import forms
from .models import Paper

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ('title', 'pdf')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
