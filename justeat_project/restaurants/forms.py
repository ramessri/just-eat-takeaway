from django import forms

class PostcodeForm(forms.Form):
    postcode = forms.CharField(label="Postcode", max_length=8)  # for UK postcodes