from django import forms
from .models import Link

class LinkShortener(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('link',)
