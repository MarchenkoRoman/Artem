from django import forms


class TranslationForm(forms.Form):
    text = forms.CharField()
