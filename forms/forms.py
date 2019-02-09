from django import forms

class Staff_form(forms.Form):
    name = forms.CharField(required=True)
    email=forms.EmailField()
    age=forms.IntegerField()
    birthday=forms.DateField()
    img=forms.ImageField()
