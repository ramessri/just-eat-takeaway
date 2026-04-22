import re

from django import forms
from django.core.validators import RegexValidator

UK_POSTCODE_REGEX = r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$"


class PostcodeForm(forms.Form):
    postcode = forms.CharField(
        label="Postcode",
        max_length=8,
        validators=[
            RegexValidator(
                regex=UK_POSTCODE_REGEX,
                message="Enter a valid UK postcode (e.g. EC4M 7RF).",
                flags=re.IGNORECASE,
            )
        ],
    )

    def clean_postcode(self):
        return self.cleaned_data["postcode"].upper().replace(" ", "")