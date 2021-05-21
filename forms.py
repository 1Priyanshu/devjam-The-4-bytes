from django import forms
from django.forms import fields
from .models import Rating, post



class Reviewform(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['comment']
        