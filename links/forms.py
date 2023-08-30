from django import forms

from .models import Link

# form models below
# class CreateLinkForm(forms.Form):
#     name = forms.CharField(max_length=120)
#     url = forms.URLField(max_length=240)
#     slug = forms.SlugField(required=False)


class CreateLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["name", "url"]
