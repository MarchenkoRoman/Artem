from django import forms


class TranslationForm(forms.Form):
    raw_information = forms.CharField()
    mask_char = forms.CharField(min_length=1, max_length=1)
    digits_to_hide = forms.IntegerField(min_value=0, max_value=9)
