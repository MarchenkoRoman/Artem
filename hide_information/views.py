from django.shortcuts import render
from django.http import HttpResponse

import re

from .forms import TranslationForm


def get_info(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            raw_information = form.cleaned_data['raw_information']
            mask_char = form.cleaned_data['mask_char']
            digits_to_hide = form.cleaned_data['digits_to_hide']
            hidden_information = hide_info(raw_information, mask_char, digits_to_hide)
            return render(request, 'translator/translator.html', {'text_raw': raw_information,
                                                                  'text_hidden': hidden_information,
                                                                  'digits': digits_to_hide,
                                                                  'mask': mask_char})

    return render(request, 'translator/translator.html',)


def hide_info(raw_information, mask_char, digits_to_hide):

    pattern_skype = re.compile(r'skype:[a-zA-Z0-9]+')
    pattern_email = re.compile(r'''[a-zA-Z0-9]([\w.\-+]+)*[a-zA-Z0-9]         
                                  @{1}
                                  (?:[a-zA-Z0-9][\w.\-+]*[a-zA-Z0-9]\.)+      
                                  [\w.\-+]+[a-zA-Z0-9]                         
                               ''',
                               re.VERBOSE)
    pattern_number = re.compile(r'\+\d{1,3}(?: [0-9]{3}){3}')

    def hide_email(matchobj):
        if matchobj.group(1):
            return matchobj.group(0)[0] + (len(matchobj.group(1)) * mask_char) + \
                   matchobj.group(0)[len(matchobj.group(1)) + 1:]
        else:
            return matchobj.group(0)

    def hide_number(matchobj):
        if matchobj.group(0):
            if digits_to_hide == 0:
                return matchobj.group(0)
            else:
                number = str(matchobj.group(0)).replace(' ', '')
                number = number[:-digits_to_hide] + mask_char * digits_to_hide
                number = list(number)
                for n in range(-9, 0, 3):
                    number.insert(n, ' ')

                return ''.join(number)

    row = re.sub(pattern_skype, 'skype:' + mask_char, raw_information)
    row = re.sub(pattern_number, hide_number, row)
    row = re.sub(pattern_email, hide_email, row)

    return row
