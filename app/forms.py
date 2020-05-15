from django import forms


class PostForm(forms.Form):
    is_boast = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        label='Boast or Roast?',
        choices=((True, 'Boast'), (False, 'Roast')),
        widget=forms.RadioSelect
    )
    content = forms.CharField(
        max_length=280,
        widget=forms.Textarea
    )
