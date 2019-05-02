from django.shortcuts import render
from django.http import HttpResponse
from .forms import TranslationForm


def hide_info(request):
    text = 'xxx'
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

        args = {'form': form, 'text': text}

    return render(request, 'translator/translator.html', {'text': text})
