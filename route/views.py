from django.shortcuts import render
from django.http import HttpResponse
from torch import constant_pad_nd

from route.generate.ruTitle import RuTitle
from .generate.ruGPT3 import RuGPT3


def gpt3(request):
    print("Getting request to generate text")
    text = request.GET.get('text', '')
    maxLength = int(request.GET.get('maxLength', '0'))

    gen = ''

    try:
        gpt3 = RuGPT3()
        gen = gpt3.generate(text, maxLength)
    except:
        gen = text
    return HttpResponse(gen)


def title(request):
    print("Getting request to generate title")
    text = request.GET.get('text', '')

    gen = ''

    try:
        title = RuTitle()
        gen = title.generate(text)
    except:
        pass

    return HttpResponse(gen)
