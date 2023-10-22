from django.http import HttpResponse
from django.views.generic import TemplateView
import os


def helloworldfunction(request):
    returnobject = HttpResponse("<h1>hello word</h1>")
    return returnobject


class HelloWorldView(TemplateView):
    template_name = "hello.html"
