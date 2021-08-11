from django.forms import ModelForm
from .models import testimonial
from django import forms

class Testf(forms.Form):
    img = forms.ImageField()
    Name = forms.CharField(max_length=200)
    Profession = forms.CharField(max_length=300)
    Company_name = forms.CharField(max_length=300)
    feedback = forms.Textarea()


class Testform(forms.ModelForm):
    class Meta:
        model = testimonial
        fields = '__all__'