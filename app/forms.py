from django import forms

from app.models import Post


class PostForm(forms.Form):
    is_boast = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        label='Boast or Roast?',
        choices=((False, 'Boast'), (True, 'Roast')),
        widget=forms.RadioSelect
    )
    content = forms.CharField(
        max_length=280,
        widget=forms.Textarea
    )
