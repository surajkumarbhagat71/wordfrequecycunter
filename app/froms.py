from django import forms
from .models import *

class WordStockForm(forms.ModelForm):
    class Meta:
        word = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'word'}))
        model = WordStok
        fields = '__all__'